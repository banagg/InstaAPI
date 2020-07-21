import subprocess
from flask import Flask, redirect, url_for, request, jsonify
import sqlite3
import pandas as pd
import os

app = Flask(__name__)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route("/api/v1/info", methods=["GET"])
def api_all():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    conn.row_factory = dict_factory
    info = cur.execute(
        "SELECT p.id, p.url, p.owner_id FROM pro_name as p, bd_name WHERE p.id = bd_name.id"
    ).fetchall()

    f_info = []
    tag_info = []
    c_info = {}
    for i in range(0, len(info)):
        tag_info = cur.execute(
            "SELECT distinct tag_tb.tag FROM tag_tb WHERE tag_tb.id = %s" % info[i][0]
        ).fetchall()
        ftag_info = [y for x in tag_info for y in x]
        c_info = {
            "id": info[i][0],
            "url": info[i][1],
            "owner_id": info[i][2],
            "tags": ftag_info,
        }
        f_info.append(c_info)

    return jsonify(f_info)


@app.route("/ezenciel/")
def success():
    return "Currently not an active functionality"


# Requests will allow you to send HTTP/1.1 requests using Python


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        pname = request.form["pn"]
        brand = request.form["bd"]
        subprocess.call("rm -rf %s" % pname, shell=True)
        subprocess.call("rm -rf %s" % brand, shell=True)
        subprocess.call(
            "instagram-scraper %s --tag --media-metadata --media-types none -m 100"
            % pname,
            shell=True,
        )
        subprocess.call(
            "instagram-scraper %s --tag --media-metadata --media-types none -m 100"
            % brand,
            shell=True,
        )

        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        conn.execute("DELETE FROM pro_name")
        conn.execute("DELETE FROM bd_name")
        conn.execute("DELETE FROM tag_tb")

        with open(os.getcwd() + "/%s/%s.json" % (pname, pname)) as f:
            df = pd.read_json(f)
        with open(os.getcwd() + "/%s/%s.json" % (brand, brand)) as g:
            dg = pd.read_json(g)

        for i in range(0, len(df["GraphImages"])):
            conn.execute(
                "INSERT OR IGNORE INTO pro_name (id, url, owner_id) VALUES (?, ?, ?)",
                (
                    df["GraphImages"][i]["id"],
                    df["GraphImages"][i]["display_url"],
                    df["GraphImages"][i]["owner"]["id"],
                ),
            )
        for i in range(0, len(df["GraphImages"])):
            try:
                for j in range(0, len(df["GraphImages"][i]["tags"])):
                    conn.execute(
                        "INSERT INTO tag_tb (id, tag) VALUES (?, ?)",
                        (df["GraphImages"][i]["id"], df["GraphImages"][i]["tags"][j]),
                    )
            except KeyError:
                pass
        for i in range(0, len(dg["GraphImages"])):
            conn.execute(
                "INSERT INTO bd_name (id) VALUES (?)", (dg["GraphImages"][i]["id"],)
            )
        conn.commit()
        conn.close()

        return redirect(url_for("api_all"))
    else:
        pname = request.args.get("pn")
        brand = request.args.get("bd")
        return redirect(url_for("success"))


if __name__ == "__main__":
    app.run(debug=True)