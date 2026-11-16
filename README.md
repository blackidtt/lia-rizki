# The Wedding of Lia & Rizki - Website Undangan Digital

Repository ini berisi kode frontend website undangan pernikahan Lia & Rizki yang siap dideploy ke **GitHub Pages**, **Netlify**, atau **Vercel**.

## 🚀 Cara Deploy ke GitHub Pages Langsung dari Folder Ini

1. Buat repository baru di [github.com](https://github.com) (misal: `lia-rizki-wedding`).
2. Buka terminal/PowerShell di folder ini:
   ```bash
   git init
   git add .
   git commit -m "Initial deploy"
   git branch -M main
   git remote add origin https://github.com/<username-anda>/<nama-repo>.git
   git push -u origin main
   ```
3. Buka GitHub > **Settings** > **Pages** > Ubah branch jadi `main` (folder `/(root)`) > **Save**.

## 💻 Menjalankan di Komputer Lokal

Cukup double-click file `start-server.bat` atau jalankan:
```bash
python -m http.server 8080
```
Lalu buka browser di: `http://localhost:8080`

## 💌 Kustomisasi Nama Tamu

Kirim link dengan parameter `?to=`:
- `https://<username>.github.io/<nama-repo>/?to=Nama+Tamu`
