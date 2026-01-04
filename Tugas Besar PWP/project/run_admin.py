from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

# ================= DATABASE =================
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'galangdanadb'

mysql = MySQL(app)

# ================= ADMIN PAGE =================
@app.route('/admin')
def admin():
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT
            id_campaign,      -- c[0]
            judul,            -- c[1]
            '-' AS kategori,  -- c[2] dummy
            '-' AS lokasi,    -- c[3] dummy
            deskripsi,        -- c[4]
            target_dana,      -- c[5]
            created_at        -- c[6]
        FROM campaign
        WHERE status_verifikasi = 'pending'
        ORDER BY created_at DESC
    """)
    campaigns = cur.fetchall()
    cur.close()

    return render_template('admin.html', campaigns=campaigns)

# ================= VERIFIKASI =================
@app.route('/admin/verifikasi/<int:id_campaign>', methods=['POST'])
def verifikasi(id_campaign):
    status = request.form['status']  # disetujui / ditolak
    status_campaign = 'aktif' if status == 'disetujui' else 'dihentikan'

    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE campaign
        SET status_verifikasi = %s,
            status_campaign = %s
        WHERE id_campaign = %s
    """, (status, status_campaign, id_campaign))

    mysql.connection.commit()
    cur.close()

    return redirect('/admin')

if __name__ == '__main__':
    app.run(debug=True)
