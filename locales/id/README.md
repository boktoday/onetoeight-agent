# OneToEight Agent: gambaran umum dan alur penyiapan

**OneToEight Agent** adalah asisten AI pribadi yang dibangun di atas
[Hermes Agent](https://hermes-agent.nousresearch.com/docs) untuk
anak muda yang sedang belajar menghidupkan **Delapan Hal Esensial**
dalam praktik harian. Ia adalah mentor yang lembut, menjalankan
irama harian berupa rencana audio, cek refleksi, dan langkah-langkah
kecil, yang diajarkan dari panduan Delapan Hal Esensial yang ikut
disertakan di dalam repo ini.

README ini adalah gambaran umum sekaligus alur kerja untuk
menjalankan agen dari awal sampai siap. Baca sekali, lalu ikuti
langkah-langkahnya.

> **Dua jalan masuk.** Ambil **jalur membangun** dan bangun agen ini
> bagian demi bagian: satu kemampuan, satu manfaat nyata, setiap
> minggu, dengan audio untuk diikuti. Atau pasang dengan alur
> penyiapan di bawah ini.
>
> **Mulai jalur membangun: <https://gladtobe.here.now/build-path/>**

> Baca ini dalam: **Bahasa Indonesia** · [English](README.md) · [Bahasa Melayu](README.ms.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Filipino](README.tl.md) · [Español](README.es.md) · [中文](README.zh.md) · [한국어](README.ko.md) · [日本語](README.ja.md)

---

## Apa produk ini

Cara terbaik bagi anak muda mempelajari Delapan Hal Esensial adalah
dengan **melakukan satu hal kecil setiap hari** selama berminggu-minggu
dan berbulan-bulan, bukan dengan membaca buku. OneToEight Agent hadir
untuk membuat irama harian itu bertahan:

- Sebuah **Menit Pagi** (Morning Minute) datang pada waktu pilihan
  murid di chat mereka (Telegram atau WhatsApp). Isinya rencana
  hari itu dalam bentuk audio singkat, plus teks.
- Sebuah **Cek Sore** (Afternoon Check-In) datang sore hari. Isinya
  pesan teks singkat: bagaimana harinya berjalan, apa selanjutnya,
  satu pertanyaan untuk direnungkan sampai besok.
- Sebuah **Sesi Rencana** (Planning Session) datang sebelum tidur.
  Ia memetakan esok: tugas sekolah, tenggat pekerjaan rumah, hal
  esensial yang sedang dikerjakan minggu ini, satu hal nyata yang
  ingin dilakukan. Agen menyusun rancangannya, murid menyuntingnya,
  dan tersimpan secara lokal. Tanpa aplikasi, tanpa akun, tanpa
  sinkronisasi cloud.
- Agen mengajar dari **panduan Delapan Hal Esensial** yang tersimpan
  di repo (`essentials/01..08/lessons/*.md`), bercabang sesuai
  tradisi yang dipilih murid.
- Panduan itu juga diterbitkan dalam **sepuluh bahasa**, bisa
  dibaca online atau diunduh sebagai paket offline untuk dipakai
  tanpa internet. Lihat `essentials/guide-editions.md`.

Agen ini tidak berceramah. Ia mengeluarkan kebijaksanaan dari dalam
diri murid lewat pertanyaan, menjaga irama dengan lembut, dan
membantu mereka mulai lagi saat tersandung, tanpa menegur.

### Dua tradisi, atau tradisimu sendiri

Setiap murid memilih satu saat onboarding. Atau beri tahu agen
tradisimu, dan agen akan membangunnya ke dalam. Agen tetap berada di
dalam tradisi yang dipilih; ia tidak pernah mencampur tradisi:

- **Kristen**: berakar pada Alkitab. Menit Pagi menyertakan ayat
  Alkitab setiap pagi, dibacakan secara alami. Cek Sore membingkai
  hari itu di dalam iman yang hidup.
- **Universal (sekuler)**: tradisi kebijaksanaan dihormati tanpa
  doktrin. Menit Pagi menyertakan refleksi atau pertanyaan singkat
  dari seorang pemikir. Cek Sore membingkai hari itu di dalam
  refleksi, rasa syukur, dan niat yang jelas.

Murid bisa mengganti tradisi nanti, tetapi pelajaran bercabang dari
titik itu seterusnya.

### Dua urutan penyampaian

Setiap murid juga memilih bagaimana Delapan Hal Esensial disajikan:

- **Sekuensial** (bawaan): berjalan dari esensial 1 sampai 8 secara
  berurutan. Ini yang paling runtut dan merupakan urutan yang
  dirancang untuk panduan. Direkomendasikan untuk murid baru.
- **Acak**: mengambil esensial mana pun pada hari mana pun,
  disesuaikan dengan kebutuhan murid hari itu (jarak waktu terlama,
  kesulitan terbaru, energi hari itu). Setiap Menit Pagi dibuka
  dengan ringkasan pengetahuan dari esensial yang dipilih plus satu
  aktivitas kecil. Terbaik untuk murid yang sudah tahu apa yang
  mereka butuhkan.

Di kedua mode, **semua delapan esensial pada akhirnya dibahas.**
Murid bisa berganti mode nanti dengan memperbarui kunci memori
`essentials_order`, tanpa perlu onboarding ulang.

### Delapan Hal Esensial (dalam urutan panduan mengajarkannya)

1. **Keheningan**: duduk diam, sendiri bersama pikiranmu sendiri
2. **Tubuh**: tidur, makanan, air, gerak, sinar matahari
3. **Keterampilan**: kecakapan dunia nyata yang berguna (memasak, memperbaiki, membangun, mengatur uang)
4. **Bela Diri Digital**: privasi, perhatian, literasi identitas
5. **Komunitas Nyata**: orang-orang yang tahu namamu
6. **Pengetahuan Tanpa Wi-Fi**: dimiliki, bukan disewakan
7. **Alam**: waktu di luar ruangan yang diresepkan, tidak bisa ditawar
8. **Keyakinan yang Teruji**: keyakinanmu, dan ia bertahan di bawah tekanan

---

## Cara kerjanya

### Lingkaran harian

```
06:00  Menit Pagi        Audio Piper TTS + teks → Telegram atau WhatsApp
        ↓
hari   Murid melakukan satu langkah kecil itu
        ↓
17:00  Cek Sore          Teks saja → Telegram atau WhatsApp
        ↓
21:00  Sesi Rencana      Teks saja → Telegram atau WhatsApp
       Agen menyusun rencana esok → murid menyunting → tersimpan lokal
        ↓
        Tidur
        ↓
        Ulangi
```

Agen memperkuat lingkaran ini tanpa mengomel. Hari yang terlewat
dimulai lagi dengan lembut. Tanpa menegur. Tanpa menggurui.

**Soal jadwal:** Waktu-waktu di atas adalah waktu lokal murid.
Daemon cron menyimpan jadwal dalam **UTC**. Jika kamu memilih pukul
6 pagi WIB (UTC+7), cron menyimpannya sebagai `0 23 * * *` (23:00
UTC). Jadwal selalu "waktu di zona waktumu", konversinya ke UTC
otomatis.

### Tugas agen di setiap kesempatan

| Kapan | Agen |
|---|---|
| Chat pertama di profil baru | Menawarkan orientasi, singkat, dengan suaranya sendiri |
| Murid berkata "atur aku" | Menjalankan `agent-onboarding` (berbasis persetujuan, bertahap) |
| Murid bertanya | Membaca `essentials/<NN-name>/lessons/*.md` yang relevan, menyintesis, mengajar |
| Cron Menit Pagi menyala | Menyusun rencana hari itu, menjalankan Piper, mengunggah, mengirim langsung |
| Cron Cek Sore menyala | Membaca Menit Pagi terakhir, menyusun refleksi singkat, mengirim sebagai teks |
| Cron Sesi Rencana menyala | Menyusun rencana esok (tugas sekolah, tenggat, esensial minggu ini, satu hal nyata), murid menyuntingnya, tersimpan lokal |
| Murid meminta pendalaman | Memakai skill `eight-essentials-curriculum`, membaca panduan, mengajar darinya |

### Yang berjalan di latar belakang

Tiga pekerjaan cron, semuanya mati sampai murid menyetujuinya saat
onboarding:

1. **Menit Pagi**: menyala pada waktu pilihan di zona waktu murid,
   setiap hari (atau hanya hari sekolah, jika diinginkan). Menghasilkan
   audio + teks dan mengirimkannya ke Telegram atau WhatsApp.
2. **Cek Sore**: menyala pada waktu sore pilihan, aturan hari yang
   sama dengan Menit Pagi. Mengirim pesan teks singkat.
3. **Sesi Rencana**: menyala sebelum tidur (bawaan pukul 9 malam),
   aturan hari yang sama. Menyusun rencana esok untuk disunting murid,
   lalu menyimpannya secara lokal.

Ketiganya **opt-in**, orientasi hanya membuatnya setelah ada
persetujuan tegas.

### Dua puluh pertanyaan harian

Kumpulan kecil pertanyaan andalan yang bisa diajukan anak muda kepada
OneToEight Agent kapan saja. Agen membaca bab panduan yang relevan,
memanfaatkan apa yang sudah ia ketahui tentang murid, dan menjawab
dengan suara mereka, dalam tradisi mereka.

Intinya **bukan** menjawab kedua puluh pertanyaan itu setiap hari.
Intinya adalah memiliki kumpulan kecil pertanyaan andalan yang
memunculkan hal-hal esensial, memancing refleksi, dan mengubah rasa
ingin tahu menjadi praktik harian. Pilih satu atau dua. Lewati
sisanya. Bergantian sepanjang minggu.

Pertanyaan-pertanyaannya ditulis dengan suara anak muda. Agen tidak
berceramah balik. Ia mengajukan pertanyaan, memberi ruang untuk
jawabannya, dan menindaklanjuti dengan satu langkah kecil.

Berkas pertanyaan lengkap ada di
`essentials/00-introduction/lessons/prompts.md`. Agen membacanya saat
murid meminta "sesuatu untuk dipikirkan", pertanyaan untuk
direnungkan, atau bantuan saat macet.

#### Menurut mode

| Mode | Pertanyaan |
|---|---|
| Refleksi diri | #1, #3, #6, #7, #12, #15, #16, #20 |
| Aktivitas | #2, #9, #13, #14, #17, #19 |
| Berpikir kritis | #5, #8, #10, #18 |
| Ritual harian | #11, #16, #20 |

#### Menurut energi

| Energi | Saran pertanyaan |
|---|---|
| Lelah, lesu | #1, #20, #11 |
| Bergelora, penasaran | #5, #10, #14 |
| Macet atau datar | #3, #9, #15 |
| Ingin merenung | #4, #6, #16, #18 |
| Ingin bergerak | #2, #9, #13, #17, #19 |

#### Menurut esensial (setiap esensial muncul setidaknya dua kali)

| Esensial | Pertanyaan yang mengarah ke sana |
|---|---|
| Keheningan | #1, #7, #9, #12, #16 |
| Tubuh | #2, #9, #14, #19 |
| Keterampilan | #8, #13, #14 |
| Bela Diri Digital | #4, #8, #18 |
| Komunitas Nyata | #6, #15, #17 |
| Pengetahuan Tanpa Wi-Fi | #3, #6, #8, #10, #11 |
| Alam | #9, #19 |
| Keyakinan yang Teruji | #1, #5, #7, #10, #16, #18 |

#### Pertanyaan berat (pakai jarang-jarang)

Pertanyaan **#1**, **#5**, **#10**, dan **#18** tergolong berat. Agen
tidak pernah mendorong-dorong memakainya. Murid harus memintanya
secara khusus. Jika murid meminta pertanyaan berat dan agen menilai
hari itu bukan waktunya, agen boleh dengan lembut menawarkan
alternatif yang lebih ringan dan menjelaskan alasannya.

#### Kedua puluh pertanyaan

| # | Pertanyaan | Mode | Energi | Esensial |
|---|----------|------|--------|------------|
| 1 | Ajukan satu pertanyaan yang mungkin tidak ingin kujawab, tapi seharusnya. | Refleksi diri | Lelah / lesu | Semua delapan (terutama Keyakinan yang Teruji, Keheningan) |
| 2 | Beri aku tugas 10 menit yang akan membuatku tidak nyaman dengan cara yang berguna. | Aktivitas | Ingin bergerak | Tubuh, Keheningan, Keyakinan yang Teruji |
| 3 | Apa yang kulakukan tiga hari lalu yang belum kulakukan lagi sejak itu? Kenapa? | Refleksi diri | Macet / datar | Pengetahuan diri, Pengetahuan Tanpa Wi-Fi |
| 4 | Pilih satu esensial yang paling lemah padaku. Apa praktik terkecil yang bisa kulakukan hari ini? | Berpikir kritis | Ingin merenung | Semua delapan (diagnostik) |
| 5 | Bantah keputusan terakhirku. Apa yang akan dikatakan seorang pengkritik yang bijak? | Berpikir kritis | Bergelora / penasaran | Pengetahuan Tanpa Wi-Fi, Keyakinan yang Teruji |
| 6 | Jika aku harus mengajari seorang murid baru satu hal yang kupelajari tahun ini, apa itu? | Refleksi diri | Ingin merenung | Pengetahuan Tanpa Wi-Fi, Komunitas Nyata |
| 7 | Di bagian mana hidupku aku sedang berpura-pura alih-alih benar-benar melakukan? Di mana aku benar-benar melakukan alih-alih berpura-pura? | Refleksi diri | Lelah / lesu | Keyakinan yang Teruji, Keheningan |
| 8 | Apa yang sedang kuserahkan ke orang lain padahal seharusnya kubangun sendiri? | Berpikir kritis | Ingin merenung | Keterampilan, Bela Diri Digital, Pengetahuan Tanpa Wi-Fi |
| 9 | Beri aku aktivitas 30 menit yang tidak butuh ponsel dan tidak butuh orang lain. | Aktivitas | Macet / datar | Tubuh, Keheningan, Alam |
| 10 | Apa satu keyakinan yang kupegang yang tidak bisa kupertahankan jika ditekan? Haruskah kutetap pegang? | Berpikir kritis | Bergelora / penasaran | Keyakinan yang Teruji, Pengetahuan Tanpa Wi-Fi |
| 11 | Ujilah aku tentang sesuatu yang kulupakan pernah kuketahui. | Ritual harian | Lelah / lesu | Pengetahuan Tanpa Wi-Fi |
| 12 | Tanyakan tentang terakhir kali aku benar-benar bosan, dan apa yang kusadari dalam keheningan itu. | Refleksi diri | Macet / datar | Keheningan, Tubuh |
| 13 | Sarankan satu hal yang bisa kuselesaikan hari ini yang sudah kumulai lebih dari seminggu lalu. | Aktivitas | Ingin bergerak | Keterampilan, Keyakinan yang Teruji |
| 14 | Tuntun aku melakukan sesuatu yang praktis yang belum kutahu caranya: memasak untuk diri sendiri, menambal ban bocor, menulis CV, mengganti ban. | Aktivitas | Bergelora / penasaran | Keterampilan, Tubuh |
| 15 | Siapa dalam hidupku yang akan datang tengah malam jika kubutuhkan? Siapa yang tidak? Kenapa? | Refleksi diri | Macet / datar | Komunitas Nyata |
| 16 | Bandingkan bagaimana aku menghabiskan waktuku hari ini dengan bagaimana aku katakan ingin menghabiskannya. Di mana selisihnya? | Ritual harian | Ingin merenung | Keyakinan yang Teruji, Keheningan |
| 17 | Beri aku pembuka percakapan yang bisa kupakai dengan satu orang yang sudah lama tidak kubicara dengan sungguh-sungguh. | Aktivitas | Ingin bergerak | Komunitas Nyata |
| 18 | Jika aku menghapus semua aplikasi di ponselku kecuali tiga, tiga apa yang harus tinggal dan kenapa? | Berpikir kritis | Ingin merenung | Bela Diri Digital, Keyakinan yang Teruji |
| 19 | Ajak aku berjalan di luar 15 menit. Apa yang sebenarnya harus kulihat, kudengar, kusadari? | Aktivitas | Ingin bergerak | Alam, Tubuh, Keheningan |
| 20 | Tutup hari ini bersamaku. Tiga hal yang terjadi, tiga hal yang kusadari, satu hal yang kusyukuri. | Ritual harian | Lelah / lesu | Semua delapan (menutup hari) |

#### Bagaimana agen memakainya

Agen membaca
`essentials/00-introduction/lessons/prompts.md` setiap kali murid
meminta pertanyaan. Ia **tidak** menempelkan daftar pertanyaan ke
murid. Ia menyebut satu, mengundang murid membacanya, dan memberi
ruang untuk jawabannya. Ia tidak pernah mengajukan tiga pertanyaan
berturut-turut.

Dalam urutan **sekuensial**, pertanyaan-pertanyaan secara alami
berkumpul di sekitar esensial yang sedang dikerjakan murid. Dalam
urutan **acak**, agen memilih pertanyaan yang cocok dengan momen itu.
Semua delapan esensial tetap tersedia di kedua mode.

---

## Ritual harian

Ini adalah peta sekilas semua ritual yang dijalankan agen: apa
isinya, kapan menyala, di mana ia mendarat, dan di mana didokumentasikan
secara rinci.

| Ritual | Kapan | Kanal | Yang terjadi |
|---|---|---|---|
| **Menit Pagi** | Setiap hari pada waktu pilihan murid (bawaan 6 pagi) | Telegram atau WhatsApp, **gelembung suara + teks** | Rencana audio untuk hari itu, fokus pada satu langkah kecil dari esensial yang sedang dikerjakan. |
| **Cek Sore** | Setiap hari pada waktu pilihan murid (bawaan 5 sore) | Telegram atau WhatsApp, **teks saja** | Refleksi tentang bagaimana hari berjalan, rencana esok, satu pertanyaan untuk direnungkan semalam. |
| **Sesi Rencana** | Setiap hari sebelum tidur pada waktu pilihan murid (bawaan 9 malam) | Telegram atau WhatsApp, **teks saja** | Agen menyusun rencana esok (tugas sekolah, tenggat PR, esensial minggu ini, satu hal nyata). Murid menyuntingnya. Tersimpan lokal. |
| **Ringkasan Esensial** | Sesuai permintaan, kapan saja murid meminta | Telegram atau WhatsApp, **pesan suara** | Ringkasan lisan 3 sampai 5 menit tentang satu esensial + daftar poin kunci singkat. |
| **Pelajaran Esensial** | Sesuai permintaan, kapan saja murid meminta | here.now, **tautan halaman HTML di chat** | Pelajaran tiga halaman tentang satu esensial dengan sumber terkutip, kutipan kunci, dan kuis singkat. |
| **Puisi Esensial** | Sesuai permintaan, kapan saja murid meminta | Telegram atau WhatsApp, **pesan suara + teks** | Puisi lisan berima tentang esensial itu, dibacakan dengan teks di bawahnya. |
| **Lagu Esensial** | Sesuai permintaan, kapan saja murid meminta | Telegram atau WhatsApp, **MP3 pesan suara + teks** | Agen menulis puisi tentang esensial itu, lalu mengubahnya menjadi lagu sungguhan via Google Lyria 3 di OpenRouter. Biaya ~$0.08 per lagu, konfirmasikan sebelum menjalankan. |
| **Video Musik Esensial** | Sesuai permintaan, kapan saja murid meminta | here.now, **tautan video MP4 di chat** | Lagu di atas, plus papan cerita gambar-gambar yang disatukan dengan audionya, dengan overlay teks puisi opsional. Biaya total ~$0.35, konfirmasikan sebelum menjalankan. |

**Harinya.** Menit Pagi membuka hari, Cek Sore menutupnya, dan Sesi
Rencana memetakan esok sebelum tidur. Tiga format sesuai permintaan
(Ringkasan / Pelajaran / Puisi) tersedia kapan pun anak muda ingin
mempelajari sebuah esensial lebih dalam daripada yang bisa dicakup
Menit Pagi dalam satu menit.

**Di mana kodenya berada.** Setiap baris menunjuk ke sebuah skill di
repo:

| Ritual | Jalur skill |
|---|---|
| Menit Pagi | `skills/hermes/morning-minute/` |
| Cek Sore | `skills/profile/afternoon-checkin/` |
| Sesi Rencana | `skills/profile/planning-session/` |
| Ringkasan, Pelajaran, Puisi, Lagu, Video Musik Esensial | `skills/profile/essential-deep-dives/` (Lagu dan Video Musik memakai `skills/creative/openrouter-lyria-music/` dan `skills/creative/poem-song-video-studio/`) |

**Persetujuan.** Tiga ritual berbasis cron (Menit Pagi, Cek Sore,
Sesi Rencana) mati sampai murid atau orang tua menyetujuinya saat
onboarding. Lima format sesuai permintaan (Ringkasan, Pelajaran,
Puisi, Lagu, Video Musik) langsung tersedia, murid tinggal meminta.
Dua format berbayar (Lagu dan Video Musik, Lyria 3 + gambar papan
cerita) memerlukan konfirmasi biaya setiap kali agen diminta
menjalankannya. Lihat [Alur penyiapan → Yang berjalan di latar
belakang](#yang-berjalan-di-latar-belakang) untuk alur opt-in yang
persis.

**Skill Lagu dan Video Musik.** Dua format berbayar itu memakai
kembali dua skill yang sudah ada, bukan menciptakan yang baru:

| Format | Skill yang mendasari | Apa yang ditambahkannya di atas `essential-deep-dives` |
|---|---|---|
| **Lagu Esensial** | `skills/creative/openrouter-lyria-music/` | Lirik PUISI → audio MP3 via Google Lyria 3 (~$0.08 per lagu). |
| **Video Musik Esensial** | `skills/creative/poem-song-video-studio/` | LAGU + ~8 gambar papan cerita + ffmpeg → MP4 (~$0.35 total). |

Kedua skill itu sudah ada di repo dengan catatan model Lyria 3
lengkap, skrip, dan pengaman biaya. Agen memuat skill dasarnya saat
murid meminta format tersebut.

**Cara menyesuaikan.** Agen memandu murid memilih waktu, zona waktu,
dan aturan hari untuk tiap ritual cron saat penyiapan. Ketiganya bisa
dijeda, dilanjutkan, atau dihapus nanti dengan
`cronjob(action="...")`. Format sesuai permintaan memilih tradisi
murid secara otomatis; suara dan panjangnya mewarisi suara Piper
Menit Pagi yang sudah dipilih.

---

## Berapa biaya menjalankannya

OneToEight Agent berjalan **bayar sesuai pemakaian**, tanpa
langganan. Kamu mengisi saldo akun OpenRouter dan agen menariknya
dari kredit itu.

| Pengeluaran | Jumlah | Catatan |
|---|---|---|
| **Bulan pertama** | **sekitar $20** | Mencakup penyiapan plus bulan pertama pemakaian nyata saat murid menyesuaikan diri |
| **Selanjutnya** | **$5–$10 sebulan** | Pemakaian harian ringan dengan model berbiaya rendah |

Profil ini bersandar pada model berbiaya rendah untuk pekerjaan
rutin:

- **DeepSeek V4 Flash**: bawaan untuk chat harian dan pelajaran.
- **Google Gemini 3.7 Flash**: cadangan cepat untuk tugas singkat.
- **Model sumber terbuka** (tier gratis atau nyaris gratis): untuk
  pekerjaan dasar bervolume tinggi yang tidak perlu model terdepan.

Tier gratis berganti dari bulan ke bulan, jadi daftarnya berubah.
Lihat daftar model gratis terkini di
<https://openrouter.ai/openrouter/free>. Profil ini secara bawaan
memilih opsi murah dan hanya mengambil model yang lebih besar saat
sebuah tugas benar-benar membutuhkannya.

---

## Tutorial

Lebih suka panduan langkah demi langkah? Hub tutorial mengumpulkan
semua halaman penyiapan di satu tempat:

- **Jalur membangun**: tujuh halaman yang mengajar dengan cara membangun: agen dibuat bagian demi bagian, dengan audio untuk diikuti. Mulai di <https://gladtobe.here.now/build-path/>.
- **Kurikulum onboarding**: tujuh halaman: kursus pemasangan, dari instalasi pertama sampai agen tersambung ke chat.
- **Lembar panduan**: penyiapan dalam satu halaman, dalam tiga bahasa.

Buka hub-nya di <https://gladtobe.here.now/hub-tutorials.html>. Alur
di bawah ini mencakup hal yang sama secara teks, langkah demi langkah.

---

## Alur penyiapan

### 1: Prasyarat (sekali saja, di mesin)

Yang kamu butuhkan:

- **Hermes Agent** terpasang. Cek cepat: `hermes --version`. Lihat
  [panduan instalasi](https://hermes-agent.nousresearch.com/docs).
- **Python 3.10 sampai 3.13** (bukan shim Windows Store, tetapi
  instalasi sungguhan). `python --version`.
- **Piper TTS.** Instalasi yang berfungsi. Lihat Langkah 2 di bawah.
- **ffmpeg** untuk konversi WAV → OGG. `ffmpeg -version`.
- **Kunci penyedia model.** Profil ini secara bawaan memakai
  `openrouter + deepseek-v4-flash`. Satu kunci membuka katalog model
  yang luas, termasuk model tier gratis dan multimodal (gambar,
  audio). Daftar gratis di <https://openrouter.ai/> dan tambahkan
  kuncinya dengan `hermes setup`. OpenCode Go adalah cadangannya.
- **Kunci API Jina AI gratis** untuk pencarian web. Daftar gratis
  di <https://jina.ai/>, tanpa kartu kredit. Tier gratisnya cukup
  untuk pemakaian harian anak muda.
- **Sebuah bot Telegram** (direkomendasikan) atau jembatan WhatsApp.
  Telegram jauh lebih mudah, lihat Langkah 4.

### 2: Ekstrak profilnya (sekali saja)

Kamu menerima profil ini sebagai berkas zip, `onetoeight-agent-id.zip`.
Ekstrak berkas itu ke dalam `~/.hermes/profiles/` sehingga menjadi
`~/.hermes/profiles/onetoeight-agent/`, lalu:

```bash
mkdir -p ~/.hermes/profiles
# ekstrak onetoeight-agent-id.zip ke dalam folder ini
hermes profile use onetoeight-agent
hermes chat
```

> **Catatan:** direktori profilnya bernama `onetoeight-agent`, bukan
> `onetoeight`. Sesuaikan perintah yang menyebut jalur profil.

Untuk pembaruan nanti: unduh zip yang baru dan ekstrak ke folder
sementara. Salin berkas-berkas baru itu masuk, tetapi **jangan
menghapus** folder `memories/` dan sesi yang tercatat. Berkas
`LOCALE.md` di akar folder mencatat dari build mana versi ini
berasal.

### 3: Chat pertama → orientasi

Pada chat pertama, agen membuka dengan:

> "Sebelum kita mulai, mau aku tuntun penyiapannya? Cuma butuh
> beberapa menit dan membuat alat, memori, dan menit pagimu bekerja
> sesuai keinginanmu. Atau kita lewati saja dan langsung mulai."

Jawab ya (atau cukup minta *"bantu aku menyiapkan profilku"* kapan
saja). Skill `agent-onboarding` akan berjalan.

### 4: Orientasi (berbasis persetujuan)

Orientasinya berupa percakapan. Agen mengajukan satu kelompok kecil
pertanyaan terkait sekaligus dan **berhenti di setiap gerbang
kredensial**. Ia tidak pernah meminta kunci atau token di chat.

Inilah yang dicakupnya, secara berurutan:

| Langkah | Yang terjadi | Di mana kamu menambahkan sesuatu |
|---|---|---|
| 1. Identitas | Nama (namamu, nama murid, nama agen), gaya balasan, dan bahasa untuk panduan, pelajaran dan pesan | Tersimpan di memori profil |
| 2. Profil dan kehidupan | Usia, lokasi, situasi tempat tinggal, bentuk minggu, 3 minat, tujuan fokus, lingkaran pertemanan, penghambat, hal yang tidak boleh dibahas | Tersimpan di memori profil |
| 3. Tradisi | Kristen, Universal, atau tradisimu sendiri | Tersimpan di memori profil |
| 4. Pemasangan Piper + suara | Memverifikasi Piper bekerja, memilih suara, mengunduh model suara | Model suara di `piper-voices/` |
| 5. Kunci API Jina | Daftar gratis, tambahkan ke `.env`, agen memverifikasi dengan pencarian sungguhan | `JINA_API_KEY=` di `.env` |
| 6. Kanal pengiriman | Kredensial bot Telegram atau WhatsApp | `TELEGRAM_BOT_TOKEN=` / `WHATSAPP_*` di `.env` |
| 7. Panduan Delapan Hal Esensial | Memastikan berkas pelajaran ada di `essentials/01..08/lessons/`, dan membagikan edisi panduan dalam bahasa murid (`essentials/guide-editions.md`) | Berkas di repo |
| 8. Memori | Mnemosyne direkomendasikan (lokal, tanpa akun eksternal) | `hermes memory setup` |
| 9. Jadwal Menit Pagi | Jam berapa, zona waktu apa, hari apa saja | Dibuat sebagai pekerjaan cron |
| 10. Jadwal Cek Sore | Jam berapa, zona waktu apa, hari apa saja | Dibuat sebagai pekerjaan cron |
| 11. Jadwal Sesi Rencana | Jam berapa (bawaan 9 malam), zona waktu apa, hari apa saja | Dibuat sebagai pekerjaan cron |
| 12. Token Router (opsional) | Plugin yang mempersempit permukaan alat | `plugins.enabled` di `config.yaml` |

Di akhir, agen menampilkan ringkasan **Usulan penyiapan** dan menunggu
persetujuan tegasmu sebelum menerapkan apa pun.

### 5: Verifikasi tiap bagian

Sebelum Menit Pagi pertama berjalan sesuai jadwal, verifikasi setiap
komponen:

```bash
# Piper works — test synthesis (paths vary by OS; see below)
echo "The Morning Minute is ready." | piper -m piper-voices/en/en_US/joe/medium/en_US-joe-medium.onnx -f /tmp/piper-test.wav

# Jina works
curl -s -H "Authorization: Bearer ***" \
  "https://s.jina.ai/https://hermes-agent.nousresearch.com/docs"
# → clean snippet of the docs page means it works

# Telegram bot works (sends a test message)
# Use the test script in Step 3 of the Telegram setup below.
# If you get "chat not found", you must first send any message to your bot in Telegram.

# Guide MD files are present
for d in essentials/*/lessons/; do echo "--- $d ---"; ls "$d"; done

# Mnemosyne is configured
hermes memory status

# Cron jobs are queued
cronjob(action="list")
```

**Lokasi biner Piper menurut platform:**

| Platform | Jalur umum |
|---|---|
| Linux | `/data/.hermes/bin/piper/piper` |
| macOS (Homebrew) | `/opt/homebrew/bin/piper` |
| macOS (manual) | `~/Library/Piper/piper` |
| Windows | `C:/Users/<you>/.openhuman/bin/piper/piper/piper.exe` |
| Windows (pip) | `pip install piper-tts`, lalu `piper` di PATH |

Orientasi akan mencari Piper dan menemukannya jika ada di PATH-mu.
Jika terpasang di tempat yang tidak biasa, orientasi akan menanyakan
jalurnya.

**Penyimpanan model suara** (isi sekali, pakai selamanya):

| Suara | Lokal | Jalur Hugging Face |
|---|---|---|
| `en_US-joe-medium` | US pria | `rhasspy/piper-voices/resolve/main/en/en_US/joe/medium/en_US-joe-medium.onnx` |
| `en_US-amy-medium` | US wanita | `rhasspy/piper-voices/resolve/main/en/en_US/amy/medium/en_US-amy-medium.onnx` |
| `en_GB-alan-medium` | UK pria | `rhasspy/piper-voices/resolve/main/en/en_GB/alan/medium/en_GB-alan-medium.onnx` |
| `en_GB-jenny_dioco-medium` | UK wanita | `rhasspy/piper-voices/resolve/main/en/en_GB/jenny_dioco/medium/en_GB-jenny_dioco-medium.onnx` |
| `en_AU-natasha-medium` | AU wanita | `rhasspy/piper-voices/resolve/main/en/en_AU/natasha/medium/en_AU-natasha-medium.onnx` |

Pola pengambilannya (contoh, Joe di Linux):

```bash
mkdir -p ~/.hermes/piper-voices/en/en_US/joe/medium
curl -sL --fail \
  "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/joe/medium/en_US-joe-medium.onnx" \
  -o ~/.hermes/piper-voices/en/en_US/joe/medium/en_US-joe-medium.onnx
curl -sL --fail \
  "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/joe/medium/en_US-joe-medium.onnx.json" \
  -o ~/.hermes/piper-voices/en/en_US/joe/medium/en_US-joe-medium.onnx.json
```

### 6: Jadwal pertama kali berjalan

Menit Pagi menyala pada waktu terjadwal berikutnya di zona waktu
murid. Ia menghasilkan audio (Piper), mengunggahnya ke here.now untuk
URL publik, lalu mengirimkan audio itu langsung ke Telegram melalui
unggahan multipart, **bukan** lewat tautan `MEDIA:<url>` (konfigurasi
Cloudflare here.now memblokir bot pengambil berkas Telegram). Cek
Sore menyala pada waktu sore terjadwal berikutnya.

### 7: Operasi sehari-hari

Murid tidak berinteraksi dengan agen lewat terminal setiap hari. Chat
Telegram atau WhatsApp **adalah** permukaan hariannya:

- **Menit Pagi** datang sebagai gelembung suara + rencana teks.
- **Cek Sore** datang sebagai teks.
- **Sesi Rencana** datang sebelum tidur sebagai teks, agen menyusun
  rencana esok (tugas sekolah, tenggat PR, esensial minggu ini, satu
  hal nyata), murid menyuntingnya, dan tersimpan lokal. Lihat
  `skills/profile/planning-session/`.
- **Balas cek sorenya** dengan satu baris catatan tentang bagaimana
  harimu berjalan. Agen menyimpan ringkasannya dan memakainya sebagai
  panggilan balik di Menit Pagi besok.
- **Ajukan pertanyaan kapan saja.** "Seperti apa sebenarnya keyakinan
  yang teruji?" "Bagaimana cara menemukan komunitas yang nyata?" Agen
  membaca panduan dan mengajar.

#### Cara belajar lebih dalam (sesuai permintaan)

Di luar irama harian, murid bisa meminta format yang lebih dalam
tentang esensial apa pun. Semuanya ditangani skill
`essential-deep-dives` (lihat `skills/profile/essential-deep-dives/`),
dan semuanya cukup dengan meminta:

- **Ringkasan Esensial**: poin-poin kunci satu esensial dalam bahasa
  sederhana, plus **pesan suara** 3 sampai 5 menit yang dihasilkan
  agen (Piper) dan dijatuhkan ke chat supaya bisa didengarkan sambil
  berjalan atau mengerjakan sesuatu.
- **Pelajaran Esensial**: **pelajaran tiga halaman** yang indah,
  dibangun sebagai halaman HTML dan diterbitkan ke akun **here.now**
  rumah tangga. Ia mengajarkan esensial itu dengan **sumber terkutip**
  (diteliti via API Jina setiap kali pelajaran butuh bahan yang tidak
  dimiliki panduan), **kutipan kunci**, dan **kuis** singkat yang
  dijawab murid di halamannya. Agen mengirim tautannya di chat.
- **Puisi Esensial**: **puisi lisan** berima tentang esensial itu,
  dibacakan sebagai pesan suara dengan teks di bawahnya supaya murid
  bisa membaca sambil mendengarkan.
- **Lagu Esensial**: agen menulis puisi orisinal tentang esensial
  itu, lalu mengubahnya menjadi lagu sungguhan (MP3) via
  `google/lyria-3-pro-preview` di OpenRouter (~$0.08 per lagu).
  Pesan suaranya diputar di chat, teks puisinya menyusul.
  Konfirmasikan biaya sebelum menjalankan.
- **Video Musik Esensial**: Lagu di atas, plus papan cerita berisi
  bingkai gambar yang disatukan dengan audionya dan overlay teks
  puisi opsional (~$0.35 total untuk lagu + gambar papan cerita +
  perakitan ffmpeg). Diterbitkan sebagai MP4 ke here.now, tautannya
  masuk ke chat. Konfirmasikan biaya sebelum menjalankan.

Agen membaca panduan sebelum menyusun semuanya, bercabang sesuai
tradisi murid, dan menyesuaikannya dengan profil murid, aturan yang
sama dengan skill kurikulum.

### 8: Pemeliharaan

Sesekali:

- `hermes update`: menarik pustaka skill standar Hermes ke dalam
  profil (skill terkurasi tidak pernah ditimpa).
- `git -C ~/.hermes/profiles/onetoeight-agent pull`: mengambil
  perbaikan dari hulu untuk panduan atau skill.
- `cronjob(action="list")`: memastikan kedua pekerjaan masih terjadwal.

---

## Yang kamu atur di `.env`

Profil ini menyertakan `.env.example` yang menunjukkan setiap
variabel. Berikut yang sebenarnya kamu isi.

### Wajib (penyiapan apa pun)

```bash
# Model provider key
OPENAI_API_KEY=...          # or your provider's key name

# Web search (free)
JINA_API_KEY=jina_xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### Wajib untuk pengiriman Telegram

```bash
# Get these from @BotFather in Telegram
TELEGRAM_BOT_TOKEN=1234567890:ABCDefghijklmnopqrstuvwxyz
TELEGRAM_CHAT_ID=123456789
```

> **Catatan penyiapan Telegram:** setelah membuat bot via @BotFather,
> kamu **harus mengiriminya setidaknya satu pesan** (misalnya `/start`)
> sebelum agen bisa mengirim kepadamu. Bot yang belum pernah menerima
> pesan akan gagal mengirim secara diam-diam.

Untuk menemukan chat ID-mu: kirimi `@userinfobot` pesan di Telegram
dan ia akan membalas dengan ID numerikmu.

### Wajib untuk audio (Menit Pagi)

```bash
# here.now is a site publisher, not a drive. The API key is all you need.
# DRIVE_ID is not used by the audio publish flow — ignore it if you see it.
HERENOW_API_KEY=hn_xxxxxxx
```

> **Catatan soal here.now:** audionya diunggah via API publish here.now,
> yang memberi URL publik. URL ini dikirim ke Telegram lewat unggahan
> multipart, jadi **tidak** memerlukan DRIVE_ID. Jika kamu melihat
> `HERENOW_DRIVE_ID` di dokumen atau contoh lama, itu warisan dan tidak
> dipakai alur pengiriman audio saat ini.

### Integrasi opsional

```bash
# Notion
NOTION_API_KEY=...

# GitHub (for tracking, opening issues)
GITHUB_TOKEN=...

# Bluesky (if you publish there)
BLUESKY_HANDLE=...
BLUESKY_APP_PASSWORD=...
```

### Hal-hal yang BUKAN variabel env

- **Jalur model suara**: tersimpan di memori profil, bukan env.
  Jalurnya spesifik per mesin.
- **Jadwal cron**: diatur via `cronjob(action="create", ...)`,
  tersimpan di registri cron, bukan env.
- **Jalur biner Piper**: tersimpan di memori profil.
- **Mnemosyne**: lokal, tanpa kunci.

---

## Isi repo ini

```
onetoeight-agent/
├── README.md                              ← berkas ini
├── SOUL.md                                ← persona dan suara operasional
├── AGENTS.md                              ← prinsip operasional
├── profile.yaml                           ← deskriptor profil
├── config.yaml                            ← konfigurasi runtime Hermes
├── .env.example                           ← setiap variabel, dengan komentar
├── .gitignore
├── LICENSE                                ← MIT
│
├── essentials/                            ← konten sumber Delapan Hal Esensial
│   ├── 00-introduction/lessons/
│   │   ├── christian.md                   ← Pendahuluan (edisi Kristen)
│   │   └── universal.md                   ← Pendahuluan (edisi Universal)
│   ├── 01-silence/
│   │   ├── SKILL.md                       ← catatan mengajar agen untuk esensial ini
│   │   ├── lessons/
│   │   │   ├── README.md                 ← skema berkas
│   │   │   ├── christian.md               ← Bab 1 (edisi Kristen)
│   │   │   └── universal.md               ← Bab 1 (edisi Universal)
│   │   └── activities/README.md
│   ├── 02-body/        (struktur yang sama)
│   ├── 03-skills/      (struktur yang sama)
│   ├── 04-digital-self-defence/
│   ├── 05-community/
│   ├── 06-knowledge/
│   ├── 07-nature/
│   ├── 08-faith/
│   │   ├── lessons/
│   │   │   ├── christian.md               ← Keyakinan yang Teruji + Kustomisasi Kristen
│   │   │   └── universal.md               ← Keyakinan yang Teruji + Kustomisasi Sekuler
│   │   └── activities/README.md
│   ├── 09-conclusion/lessons/{christian,universal}.md
│   ├── 10-before-after/lessons/{christian,universal}.md
│   └── guide-editions.md                  ← panduan online dalam sepuluh bahasa
│
├── skills/
│   ├── hermes/                            ← skill terkurasi Hermes
│   │   ├── agent-onboarding/  ← orientasinya
│   │   ├── morning-minute/                ← rencana harian + audio
│   │   ├── hermes-mnemosyne/              ← penyedia memori
│   │   ├── mnemosyne-maintenance/
│   │   └── skill-auditor/
│   └── profile/                       ← skill milik profil sendiri
│       ├── afternoon-checkin/           ← refleksi sore
│       ├── eight-essentials-curriculum/   ← mengajar dari panduan
│       ├── essential-deep-dives/          ← format ringkasan, pelajaran, puisi
│       └── setup-walkthrough/            ← penyiapan Piper, Jina, kanal
│
├── plugins/hermes-token-router/           ← plugin opsional penyempit alat
├── memories/                              ← benih praktik operasional umum
└── skins/onetoeight.yaml                 ← tema warna
```

> **Skill Hermes standar** (web, terminal, github, creative, dll.)
> ditarik oleh `hermes update` dan bukan bagian dari repo ini. Mereka
> terdaftar di pustaka standar, bukan di sini.

---

## Referensi konfigurasi

### Penyedia model (`config.yaml`)

```yaml
model:
  default: deepseek-v4-flash
  provider: openrouter
fallback_providers:
  - provider: opencode
    model: deepseek-v4-flash
```

Ubah `provider` dan `default` untuk berganti. OpenRouter menjadi
bawaan karena satu kunci membuka katalog terluas: model gratis plus
model multimodal (gambar, audio) tanpa berpindah penyedia. Rantai
cadangan hanya berjalan saat penyedia utamanya tidak tersedia.

### Toolset (`config.yaml`)

Setiap toolset CLI **aktif secara bawaan**. Orientasi memandu murid
meninjau masing-masingnya. Untuk menonaktifkan secara manual:

```bash
hermes --profile onetoeight-agent tools
# Or start with a specific set:
hermes --profile onetoeight-agent chat --toolsets "web,terminal,file,memory"
```

Toolset `tts` harus tetap aktif untuk Menit Pagi.

### Pekerjaan cron

Buat via orientasi. Untuk mengelola secara manual:

```python
# List
cronjob(action="list")

# Create Morning Minute (UTC schedule — 6am AEST = 20:00 UTC)
cronjob(
    action="create",
    schedule="0 20 * * *",
    name="Morning Minute",
    prompt="""You are running the student's Morning Minute.
    Use the morning-minute skill. The student's tradition is
    <christian/universal>. Generate the day's plan, run Piper TTS,
    upload to here.now, deliver via multipart upload to Telegram.
    Do not write memories. Deliver only the final voice + text.""",
    skills=["morning-minute"],
    deliver="telegram",
)

# Weekdays only Morning Minute (6am, Mon–Fri)
cronjob(
    action="create",
    schedule="0 20 * * 1-5",
    name="Morning Minute",
    ...
)

# Pause without deleting
cronjob(action="pause", job_id="<id>")

# Resume
cronjob(action="resume", job_id="<id>")

# Remove (requires approval — deletes the schedule permanently)
cronjob(action="remove", job_id="<id>")
```

Lihat `skills/hermes/morning-minute/SKILL.md` untuk kontrak lengkap
cron Menit Pagi.

> **Pengiriman cron:** sesi TUI/CLI tidak punya kanal pengiriman
> langsung. Jika kamu ingin diberi tahu saat cron menyala, setel
> `deliver="telegram"` (atau `deliver="all"`) saat membuatnya. Kalau
> tidak, outputnya disimpan lokal dan bisa dilihat via
> `cronjob(action="list")`.

---

## Jebakan umum

| Gejala | Kemungkinan penyebab | Perbaikan |
|---|---|---|
| Piper gagal dimuat | Jalur model suara salah, atau belum diunduh | Jalankan ulang langkah Piper di orientasi |
| Audio Menit Pagi senyap atau terpotong | Teks input TTS terpotong | Pastikan berkas teksnya lengkap sebelum sintesis |
| Pengiriman Telegram gagal dengan "chat not found" | Bot belum pernah menerima pesan | Buka Telegram, temukan botmu, kirim `/start` |
| Audio Telegram tidak muncul | Memakai `MEDIA:<url>` dengan URL here.now | Pakai unggahan multipart via `sendVoice` (skill-nya menangani ini) |
| Cron menyala di waktu yang salah | Kebingungan UTC | Cron menyimpan UTC. 6 pagi WIB = `0 23 * * *`. 6 pagi WITA = `0 22 * * *` |
| Jadwal tertulis harian tapi hanya menyala di hari sekolah | Format cron salah | `0 6 * * *` = setiap hari. `0 6 * * 1-5` = Sen–Jum |
| Pencarian Jina tidak menghasilkan apa-apa | Kunci belum ada di `.env` atau salah | Uji dengan `curl -H "Authorization: Bearer ***" "https://s.jina.ai/"` |
| Agen memberi konten tradisi yang salah | Tradisi belum ada di memori | Jalankan ulang langkah tradisi di orientasi |
| Berkas pelajaran tidak terbaca | Sufiks `.christian.md` atau `.universal.md` hilang | Cek `ls essentials/<NN>/lessons/`, nama berkas harus bersufiks benar |

---

## Plugin Token Router (opsional)

Token Router adalah plugin Hermes opsional yang **mempersempit
permukaan alat** yang ditampilkan ke agen, bukan ke murid. Saat
aktif, agen melihat lebih sedikit alat secara bawaan, yang bisa
mengurangi pemakaian token dan menjaga agen tetap fokus pada
pekerjaan Delapan Hal Esensial.

Ia **tidak** menyembunyikan fitur dari murid. Murid tetap bisa
bertanya apa saja; router hanya memengaruhi apa yang dipilih agen
secara otomatis.

Aktifkan jika:
- Kamu ingin menjaga agen tetap fokus mengajar, bukan pada kode atau analisis data.
- Pemakaian token menjadi perhatian.

Biarkan mati jika:
- Murid (atau orang tua) ingin seluruh permukaan alat tersedia.

Untuk mengaktifkan: `hermes plugins enable hermes-token-router`
(setelah `hermes profile use onetoeight-agent`).

---

## Lisensi

MIT, lihat `LICENSE`.

Persona OneToEight Agent adalah arketipe asisten orisinal yang
ditulis untuk proyek ini. Konten panduan Delapan Hal Esensial berasal
dari onetoeight *Eight Essentials* Edisi Universal V.3.0.0, disertakan
dengan izin untuk digunakan di dalam profil ini.
