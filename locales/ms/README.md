# OneToEight Agent: gambaran keseluruhan dan aliran persediaan

**OneToEight Agent** ialah pembantu AI peribadi yang dibina atas
[Hermes Agent](https://hermes-agent.nousresearch.com/docs) untuk
orang muda yang sedang belajar menghidupkan **Lapan Esensial** dalam
kehidupan harian. Ia ialah mentor yang lembut yang menjalankan irama
harian: pelan audio, semakan renungan, dan tindakan kecil, semuanya
diajarkan daripada panduan Lapan Esensial yang disertakan dalam repo.

README ini ialah gambaran keseluruhan dan aliran untuk memfungsikan
agen ini dari awal hingga siap. Baca sekali, kemudian ikuti
langkah-langkahnya.

> **Dua cara untuk bermula.** Ikuti **build path** dan bina agen ini
> bahagian demi bahagian: satu keupayaan, satu hasil, setiap minggu,
> dengan audio untuk diikuti. Atau pasang ia dengan aliran persediaan
> di bawah.
>
> **Mulakan build path: <https://gladtobe.here.now/build-path/>**

> Baca ini dalam: **Bahasa Melayu** · [English](README.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [Filipino](README.tl.md) · [Español](README.es.md) · [中文](README.zh.md) · [한국어](README.ko.md) · [日本語](README.ja.md)

---

## Apa produk ini

Orang muda paling baik mempelajari Lapan Esensial dengan
**melakukan satu perkara kecil setiap hari** selama berminggu-minggu
dan berbulan-bulan, bukan dengan membaca buku. OneToEight Agent
wujud untuk menjadikan irama harian itu kekal:

- **Minit Pagi** (Morning Minute) tiba pada masa yang dipilih dalam
  sembang pelajar (Telegram atau WhatsApp). Ia ialah pelan audio
  ringkas untuk hari itu, bersama teks.
- **Semakan Petang** (Afternoon Check-In) tiba pada waktu petang. Ia
  ialah mesej teks ringkas: bagaimana hari itu berlalu, apa
  seterusnya, satu soalan untuk direnungkan sepanjang malam.
- **Sesi Perancangan** (Planning Session) tiba sebelum tidur. Ia
  memetakan hari esok: tugasan sekolah, tarikh akhir kerja sekolah,
  esensial yang sedang dikerjakan minggu ini, satu perkara dunia
  sebenar yang ingin dilakukan. Agen merangka pelan itu, pelajar
  menyuntingnya, dan ia disimpan secara tempatan -- tanpa aplikasi,
  tanpa akaun, tanpa penyegerakan awan.
- Agen mengajar daripada **panduan Lapan Esensial** yang disimpan
  dalam repo (`essentials/01..08/lessons/*.md`), bercabang mengikut
  tradisi pilihan pelajar.
- Panduan itu juga diterbitkan dalam **sepuluh bahasa** -- baca
  dalam talian, atau muat turun sebagai pek luar talian untuk
  digunakan tanpa internet. Lihat `essentials/guide-editions.md`.

Agen ini tidak memberi syarahan. Ia mengeluarkan kebijaksanaan
daripada pelajar melalui soalan, memegang irama itu dengan lembut,
dan membantu mereka bermula semula apabila tersasar -- tanpa
memarahi.

### Dua tradisi, atau tradisi anda sendiri

Setiap pelajar memilih satu semasa onboarding. Atau beritahu agen
tradisi anda dan ia akan membinanya. Agen ini kekal dalam tradisi
yang dipilih; ia tidak pernah mencampurkan tradisi:

- **Kristian** -- berpaut pada Alkitab. Minit Pagi mengandungi ayat
  Alkitab setiap pagi, dibaca secara semula jadi. Semakan itu
  membingkaikan hari dalam iman yang hidup.
- **Universal (sekular)** -- tradisi kebijaksanaan dihormati tanpa
  doktrin. Minit Pagi mengandungi renungan ringkas atau soalan
  daripada seorang pemikir. Semakan itu membingkaikan hari dalam
  renungan, kesyukuran, dan niat.

Pelajar boleh menukar tradisi kemudian, tetapi pelajaran bercabang
dari saat itu seterusnya.

### Dua urutan penyampaian

Setiap pelajar juga memilih bagaimana Lapan Esensial disampaikan:

- **Berurutan** (default) -- melalui esensial 1 hingga 8 mengikut
  urutan. Ini yang paling koheren dan inilah urutan yang ditulis
  dalam panduan itu. Disyorkan untuk pelajar baharu.
- **Rawak** -- tarik mana-mana esensial pada mana-mana hari,
  dipadankan dengan apa yang pelajar itu nampak perlukan pada hari
  itu (jurang terpanjang, perjuangan terkini, tenaga hari itu).
  Setiap Minit Pagi dibuka dengan ringkasan pengetahuan daripada
  esensial yang dipilih serta satu aktiviti kecil. Terbaik untuk
  pelajar yang sudah tahu apa yang mereka perlukan.

Dalam kedua-dua mod, **kesemua lapan esensial akhirnya diliputi.**
Pelajar boleh bertukar kemudian dengan mengemas kini kekunci memori
`essentials_order` -- tanpa perlu onboarding semula.

### Lapan Esensial (mengikut urutan yang diajarkan panduan)

1. **Kesunyian**: duduk diam, bersendirian dengan fikiran anda sendiri
2. **Badan**: tidur, makanan, air, pergerakan, cahaya matahari
3. **Kemahiran**: kecekapan berguna dalam dunia sebenar (memasak, membaiki, membina, mengurus wang)
4. **Pertahanan diri digital**: privasi, tumpuan, literasi identiti
5. **Komuniti yang nyata**: orang yang tahu nama anda
6. **Pengetahuan tanpa Wi-Fi**: dimiliki, bukan disewa
7. **Alam**: masa yang ditetapkan di luar, tidak boleh dirunding
8. **Keyakinan yang teruji**: milik anda, dan ia bertahan di bawah tekanan

---

## Bagaimana ia berfungsi

### Kitaran harian

```
06:00  Minit Pagi        Audio Piper + teks → Telegram atau WhatsApp
        ↓
hari   Pelajar melakukan satu tindakan kecil
        ↓
17:00  Semakan Petang    Teks sahaja → Telegram atau WhatsApp
        ↓
21:00  Sesi Perancangan  Teks sahaja → Telegram atau WhatsApp
       Agen merangka pelan esok → pelajar menyunting → disimpan secara tempatan
        ↓
        Tidur
        ↓
        Ulang
```

Agen mengukuhkan kitaran itu tanpa mengomel. Hari yang terlepas
dimulakan semula dengan lembut. Tiada memarahi. Tiada bersyarah.

**Tentang jadual:** Masa yang ditunjukkan di atas adalah dalam zon
waktu tempatan pelajar. Daemon cron menyimpan jadual dalam **UTC**.
Jika anda memilih 6 pagi waktu Malaysia (UTC+8), cron menyimpannya
sebagai `0 22 * * *` (22:00 UTC). Jadual itu sentiasa "masa dalam zon
waktu anda" -- penukaran ke UTC adalah automatik.

### Tugas agen pada setiap masa

| Bila | Agen |
|---|---|
| Sembang pertama pada profil baharu | Menawarkan orientasi, secara ringkas, dengan suaranya sendiri |
| Pelajar berkata "sediakan saya" | Menjalankan `agent-onboarding` (berpagar persetujuan, berperingkat) |
| Pelajar bertanya soalan | Membaca `essentials/<NN-name>/lessons/*.md` yang berkaitan, merumus, mengajar |
| Cron Minit Pagi menyala | Menjana pelan hari itu, menjalankan Piper, memuat naik, menghantar secara terus |
| Cron Semakan Petang menyala | Membaca Minit Pagi terkini, merangka renungan ringkas, menghantar sebagai teks |
| Cron Sesi Perancangan menyala | Merangka pelan esok (tugasan sekolah, tarikh akhir, esensial minggu itu, satu perkara dunia sebenar), pelajar menyuntingnya, disimpan secara tempatan |
| Pelajar meminta penerokaan yang lebih mendalam | Menggunakan skill `eight-essentials-curriculum` -- membaca panduan, mengajar daripadanya |

### Apa yang berjalan di latar belakang

Tiga cron job, semuanya mati sehingga pelajar meluluskannya semasa
onboarding:

1. **Minit Pagi** -- menyala pada masa yang dipilih dalam zon waktu
   pelajar, setiap hari (atau hari persekolahan sahaja, jika
   dikehendaki). Menjana audio + teks dan menghantar ke Telegram
   atau WhatsApp.
2. **Semakan Petang** -- menyala pada masa petang yang dipilih,
   peraturan hari yang sama seperti Minit Pagi. Menghantar mesej
   teks ringkas.
3. **Sesi Perancangan** -- menyala sebelum tidur (default 9 malam),
   peraturan hari yang sama. Merangka pelan esok untuk disunting
   oleh pelajar, kemudian menyimpannya secara tempatan.

Ketiga-tiganya **opt-in** -- orientasi menciptanya hanya selepas
persetujuan yang jelas.

### Dua puluh soalan harian

Perpustakaan kecil soalan andalan yang boleh diajukan oleh orang
muda kepada OneToEight Agent pada bila-bila masa. Agen membaca bab
panduan yang berkaitan, menggunakan apa yang sudah diketahuinya
tentang pelajar, dan menjawab dengan suara pelajar itu, dalam
tradisinya.

Tujuannya **bukan** menjawab kesemua dua puluh setiap hari. Tujuannya
ialah mempunyai satu set kecil soalan andalan yang menyerlahkan
esensial, mengeluarkan renungan, dan mengubah rasa ingin tahu menjadi
amalan harian. Pilih satu atau dua. Langkau yang lain. Gilirkan
sepanjang minggu.

Soalan-soalan itu ditulis dalam suara orang muda. Agen tidak
bersyarah balik. Ia bertanya soalan itu, memberi ruang untuk
jawapannya, dan menyusuli dengan satu tindakan kecil.

Fail penuh soalan-soalan itu berada di
`essentials/00-introduction/lessons/prompts.md`. Agen membacanya
apabila pelajar meminta "sesuatu untuk difikirkan", soalan untuk
direnungkan, atau bantuan apabila tersekat.

#### Mengikut mod

| Mod | Soalan |
|---|---|
| Renungan diri | #1, #3, #6, #7, #12, #15, #16, #20 |
| Aktiviti | #2, #9, #13, #14, #17, #19 |
| Pemikiran kritis | #5, #8, #10, #18 |
| Ritual harian | #11, #16, #20 |

#### Mengikut tenaga

| Tenaga | Soalan yang disyorkan |
|---|---|
| Letih, tenaga rendah | #1, #20, #11 |
| Bertenaga, ingin tahu | #5, #10, #14 |
| Tersekat atau hambar | #3, #9, #15 |
| Ingin berfikir | #4, #6, #16, #18 |
| Ingin melakukan | #2, #9, #13, #17, #19 |

#### Mengikut esensial (setiap esensial muncul sekurang-kurangnya dua kali)

| Esensial | Soalan yang condong kepadanya |
|---|---|
| Kesunyian | #1, #7, #9, #12, #16 |
| Badan | #2, #9, #14, #19 |
| Kemahiran | #8, #13, #14 |
| Pertahanan diri digital | #4, #8, #18 |
| Komuniti yang nyata | #6, #15, #17 |
| Pengetahuan tanpa Wi-Fi | #3, #6, #8, #10, #11 |
| Alam | #9, #19 |
| Keyakinan yang teruji | #1, #5, #7, #10, #16, #18 |

#### Soalan berat (gunakan jarang-jarang)

Soalan **#1**, **#5**, **#10**, dan **#18** adalah berat. Agen tidak
pernah bersandar pada soalan-soalan ini. Pelajar mesti memintanya
secara khusus. Jika pelajar meminta soalan berat dan agen menilai ia
bukan hari yang sesuai, agen boleh menawarkan alternatif yang lebih
ringan dengan lembut dan menjelaskan mengapa.

#### Dua puluh soalan itu

| # | Soalan | Mod | Tenaga | Esensial |
|---|----------|------|--------|------------|
| 1 | Tanya saya satu soalan yang mungkin saya tidak mahu jawab, tetapi perlu. | Renungan diri | Letih / rendah | Kesemua lapan (terutama Keyakinan yang teruji, Kesunyian) |
| 2 | Beri saya tugasan 10 minit yang akan membuat saya tidak selesa dengan cara yang berguna. | Aktiviti | Ingin melakukan | Badan, Kesunyian, Keyakinan yang teruji |
| 3 | Apa yang saya lakukan tiga hari lalu yang tidak saya lakukan sejak itu? Mengapa? | Renungan diri | Tersekat / hambar | Mengenali diri, Pengetahuan tanpa Wi-Fi |
| 4 | Pilih satu esensial yang paling lemah pada saya. Apakah amalan terkecil yang boleh saya lakukan hari ini? | Pemikiran kritis | Ingin berfikir | Kesemua lapan (diagnostik) |
| 5 | Bidas keputusan terakhir saya. Apa yang akan dikatakan oleh pengkritik yang bijaksana? | Pemikiran kritis | Bertenaga / ingin tahu | Pengetahuan tanpa Wi-Fi, Keyakinan yang teruji |
| 6 | Jika saya perlu mengajar seorang pelajar baharu satu perkara yang saya pelajari tahun ini, apakah itu? | Renungan diri | Ingin berfikir | Pengetahuan tanpa Wi-Fi, Komuniti yang nyata |
| 7 | Di mana dalam hidup saya saya berlakon dan bukan benar-benar melakukan? Di mana saya benar-benar melakukan dan bukan berlakon? | Renungan diri | Letih / rendah | Keyakinan yang teruji, Kesunyian |
| 8 | Apa yang sedang saya serahkan kepada orang lain yang sepatutnya saya bina sendiri? | Pemikiran kritis | Ingin berfikir | Kemahiran, Pertahanan diri digital, Pengetahuan tanpa Wi-Fi |
| 9 | Beri saya aktiviti 30 minit yang tidak memerlukan telefon dan tidak memerlukan orang lain. | Aktiviti | Tersekat / hambar | Badan, Kesunyian, Alam |
| 10 | Apakah satu kepercayaan yang saya pegang yang tidak dapat saya pertahankan jika ditekan? Patutkah saya kekalkannya juga? | Pemikiran kritis | Bertenaga / ingin tahu | Keyakinan yang teruji, Pengetahuan tanpa Wi-Fi |
| 11 | Uji saya tentang sesuatu yang saya lupa saya pernah tahu. | Ritual harian | Letih / rendah | Pengetahuan tanpa Wi-Fi |
| 12 | Tanya saya tentang kali terakhir saya benar-benar bosan, dan apa yang saya perhatikan dalam kesunyian itu. | Renungan diri | Tersekat / hambar | Kesunyian, Badan |
| 13 | Cadangkan satu perkara yang boleh saya siapkan hari ini yang saya mulakan lebih seminggu lalu. | Aktiviti | Ingin melakukan | Kemahiran, Keyakinan yang teruji |
| 14 | Bimbing saya melakukan sesuatu yang praktikal yang saya belum tahu -- memberi makan diri sendiri, membaiki tayar bocor, menulis CV, menukar tayar. | Aktiviti | Bertenaga / ingin tahu | Kemahiran, Badan |
| 15 | Siapa dalam hidup saya yang akan datang pada pukul 2 pagi? Siapa yang tidak? Mengapa? | Renungan diri | Tersekat / hambar | Komuniti yang nyata |
| 16 | Bandingkan bagaimana saya menghabiskan masa hari ini dengan bagaimana saya kata saya mahu menghabiskannya. Di mana jurangnya? | Ritual harian | Ingin berfikir | Keyakinan yang teruji, Kesunyian |
| 17 | Beri saya pembuka perbualan yang boleh saya gunakan dengan seseorang yang sudah lama tidak saya bualkan dengan betul. | Aktiviti | Ingin melakukan | Komuniti yang nyata |
| 18 | Jika saya padamkan semua aplikasi di telefon saya kecuali tiga, yang mana tiga patut kekal dan mengapa? | Pemikiran kritis | Ingin berfikir | Pertahanan diri digital, Keyakinan yang teruji |
| 19 | Bawa saya keluar 15 minit -- apa yang sepatutnya saya lihat, dengar, perhatikan? | Aktiviti | Ingin melakukan | Alam, Badan, Kesunyian |
| 20 | Tamatkan hari bersama saya. Tiga perkara yang berlaku, tiga perkara yang saya perhatikan, satu perkara yang saya syukuri. | Ritual harian | Letih / rendah | Kesemua lapan (menutup hari) |

#### Bagaimana agen menggunakannya

Agen membaca
`essentials/00-introduction/lessons/prompts.md` setiap kali pelajar
meminta soalan. Ia **tidak** menampal soalan kepada pelajar. Ia
merujuk satu soalan, menjemput pelajar membacanya, dan memberi ruang
untuk jawapannya. Ia tidak pernah bertanya tiga soalan berturut-turut.

Dalam urutan penyampaian **berurutan**, soalan secara semula jadi
berkumpul di sekeliling esensial yang sedang dilalui pelajar. Dalam
urutan **rawak**, agen memilih soalan yang sepadan dengan saat itu.
Kesemua lapan esensial kekal tersedia dalam kedua-dua mod.

---

## Ritual harian

Ini ialah peta sekilas pandang bagi setiap ritual yang dijalankan
oleh agen: apa ia, bila ia menyala, di mana ia tiba, dan di mana ia
didokumentasikan secara terperinci.

| Ritual | Bila | Saluran | Apa yang berlaku |
|---|---|---|---|
| **Minit Pagi** | Setiap hari pada masa pilihan pelajar (default 6 pagi) | Telegram atau WhatsApp -- **nota suara + teks** | Pelan audio untuk hari itu, fokus pada satu tindakan kecil daripada esensial semasa. |
| **Semakan Petang** | Setiap hari pada masa pilihan pelajar (default 5 petang) | Telegram atau WhatsApp -- **teks sahaja** | Renungan tentang bagaimana hari itu berlalu, pelan untuk esok, satu soalan untuk direnungkan sepanjang malam. |
| **Sesi Perancangan** | Setiap hari sebelum tidur pada masa pilihan pelajar (default 9 malam) | Telegram atau WhatsApp -- **teks sahaja** | Agen merangka pelan esok (tugasan sekolah, tarikh akhir kerja sekolah, esensial minggu itu, satu perkara dunia sebenar). Pelajar menyuntingnya. Disimpan secara tempatan. |
| **Ringkasan Esensial** | Atas permintaan, pada bila-bila masa | Telegram atau WhatsApp -- **nota suara** | Ringkasan lisan 3 hingga 5 minit tentang satu esensial + senarai pendek mata penting secara bertulis. |
| **Pelajaran Esensial** | Atas permintaan, pada bila-bila masa | here.now -- **pautan halaman HTML dalam sembang** | Pelajaran tiga halaman tentang satu esensial, dengan sumber yang dipetik, petikan penting, dan kuiz ringkas. |
| **Puisi Esensial** | Atas permintaan, pada bila-bila masa | Telegram atau WhatsApp -- **nota suara + teks** | Puisi bersajak yang disampaikan secara lisan tentang esensial itu, dibaca dengan kuat bersama teks di bawahnya. |
| **Lagu Esensial** | Atas permintaan, pada bila-bila masa | Telegram atau WhatsApp -- **nota suara MP3 + teks** | Agen menulis puisi tentang esensial itu, kemudian mengubahnya menjadi lagu sebenar melalui Google Lyria 3 di OpenRouter. Kos ~$0.08 setiap lagu -- sahkan sebelum menjalankannya. |
| **Video Muzik Esensial** | Atas permintaan, pada bila-bila masa | here.now -- **pautan video MP4 dalam sembang** | Lagu di atas, serta papan cerita imej pegun yang dicantumkan dengan audio, dengan lapisan teks puisi sebagai pilihan. Kos ~$0.35 kesemuanya -- sahkan sebelum menjalankannya. |

**Hari itu.** Minit Pagi membuka hari, Semakan Petang menutupnya, dan
Sesi Perancangan memetakan esok sebelum tidur. Tiga format atas
permintaan (Ringkasan / Pelajaran / Puisi) tersedia bila-bila masa
orang muda ingin mempelajari sesuatu esensial dengan lebih mendalam
daripada yang mampu diliputi Minit Pagi dalam satu minit.

**Di mana kod itu berada.** Setiap baris berpaut pada satu skill
dalam repo:

| Ritual | Laluan skill |
|---|---|
| Minit Pagi | `skills/hermes/morning-minute/` |
| Semakan Petang | `skills/profile/afternoon-checkin/` |
| Sesi Perancangan | `skills/profile/planning-session/` |
| Ringkasan, Pelajaran, Puisi, Lagu, Video Muzik | `skills/profile/essential-deep-dives/` (Lagu dan Video Muzik menggunakan `skills/creative/openrouter-lyria-music/` dan `skills/creative/poem-song-video-studio/`) |

**Persetujuan.** Tiga ritual berasaskan cron (Minit Pagi, Semakan
Petang, Sesi Perancangan) mati sehingga pelajar atau ibu bapa
meluluskannya semasa onboarding. Lima format atas permintaan
(Ringkasan, Pelajaran, Puisi, Lagu, Video Muzik) tersedia
serta-merta -- pelajar hanya perlu meminta. Dua format berbayar
(Lagu dan Video Muzik, Lyria 3 + imej papan cerita) memerlukan
pelajar mengesahkan perbelanjaan setiap kali agen diminta
menyediakannya. Lihat [Aliran persediaan → Apa yang berjalan di
latar belakang](#apa-yang-berjalan-di-latar-belakang) untuk aliran
opt-in yang tepat.

**Skill Lagu dan Video Muzik.** Dua format berbayar itu menggunakan
semula dua skill yang sedia ada:

| Format | Skill asas | Apa yang ditambahnya di atas `essential-deep-dives` |
|---|---|---|
| **Lagu Esensial** | `skills/creative/openrouter-lyria-music/` | Lirik PUISI → audio MP3 melalui Google Lyria 3 (~$0.08/lagu). |
| **Video Muzik Esensial** | `skills/creative/poem-song-video-studio/` | LAGU + ~8 imej papan cerita + ffmpeg → MP4 (~$0.35 kesemuanya). |

Kedua-dua skill ini sudah wujud dalam repo dengan nota model Lyria 3
yang lengkap, skrip, dan pengawal kos. Agen memuatkan skill asas itu
apabila pelajar meminta format berkenaan.

**Cara menyesuaikan.** Agen memandu pelajar melalui pemilihan masa,
zon waktu, dan peraturan hari untuk setiap ritual cron semasa
persediaan. Ketiga-tiganya boleh dijeda, disambung semula, atau
dibuang kemudian dengan `cronjob(action="...")`. Format atas
permintaan memilih tradisi pelajar secara automatik; suara dan
panjangnya diwarisi daripada suara Piper Minit Pagi yang sudah
dipilih.

---

## Berapa kos untuk menjalankannya

OneToEight Agent berjalan secara **pay-as-you-go** -- tanpa
langganan. Anda menambah nilai pada akaun OpenRouter dan agen
mengambil daripada kredit itu.

| Perbelanjaan | Jumlah | Nota |
|---|---|---|
| **Bulan pertama** | **sekitar $20** | Meliputi persediaan serta bulan pertama penggunaan sebenar semasa pelajar menyesuaikan diri |
| **Seterusnya** | **$5–$10 sebulan** | Penggunaan harian yang ringan pada model kos rendah |

Profil ini bergantung pada model kos rendah untuk kerja rutin:

- **DeepSeek V4 Flash** -- default untuk sembang dan pelajaran harian.
- **Google Gemini 3.7 Flash** -- sandaran pantas untuk tugasan pendek.
- **Model sumber terbuka** (peringkat percuma atau hampir percuma) -- untuk kerja asas dan volum tinggi yang tidak memerlukan model frontier.

Peringkat percuma berputar setiap bulan, jadi senarai tepatnya
berubah. Lihat senarai model percuma langsung di
<https://openrouter.ai/openrouter/free>. Profil ini menggunakan
pilihan murah secara default dan hanya mengambil model yang lebih
besar apabila sesuatu tugasan benar-benar memerlukannya.

---

## Tutorial

Mahu panduan langkah demi langkah? Hab tutorial mengumpulkan
semua halaman persediaan di satu tempat:

- **Build path** -- tujuh halaman yang mengajar melalui pembinaan: agen ini dibina bahagian demi bahagian, dengan audio untuk diikuti. Mulakan di <https://gladtobe.here.now/build-path/>.
- **Kurikulum onboarding** -- tujuh halaman: kursus pemasangan, daripada pemasangan pertama sehingga agen disambungkan ke sembang.
- **Lembaran panduan** -- persediaan dalam satu halaman, dalam tiga bahasa.

Buka hab di <https://gladtobe.here.now/hub-tutorials.html>. Aliran di
bawah meliputi perkara yang sama dalam bentuk teks, langkah demi
langkah.

---

## Aliran persediaan

### 1: Prasyarat (sekali sahaja, pada mesin)

Anda perlukan:

- **Hermes Agent** yang dipasang. Semakan pantas: `hermes --version`. Lihat [panduan pemasangan](https://hermes-agent.nousresearch.com/docs).
- **Python 3.10 hingga 3.13** (bukan shim Windows Store, tetapi pemasangan sebenar). `python --version`.
- **Piper TTS.** Pemasangan yang berfungsi. Lihat Langkah 2 di bawah.
- **ffmpeg** untuk penukaran WAV → OGG. `ffmpeg -version`.
- **Kunci penyedia model.** Profil ini menggunakan `openrouter + deepseek-v4-flash` secara default. Satu kunci membuka katalog besar model, termasuk model peringkat percuma dan multimodal (imej, audio). Daftar secara percuma di <https://openrouter.ai/> dan tambah kunci dengan `hermes setup`. OpenCode Go ialah sandaran.
- **Kunci API Jina AI percuma** untuk carian web. Daftar secara percuma di <https://jina.ai/> -- tanpa kad kredit. Peringkat percuma sudah cukup untuk penggunaan harian orang muda.
- **Bot Telegram** (disyorkan) atau jambatan WhatsApp. Telegram jauh lebih mudah -- lihat Langkah 4.

### 2: Unzip profil (sekali sahaja)

Anda menerima profil ini sebagai fail zip,
`onetoeight-agent-ms.zip`. Unzip ke dalam `~/.hermes/profiles/`
supaya menjadi `~/.hermes/profiles/onetoeight-agent/`, kemudian:

```bash
mkdir -p ~/.hermes/profiles
# unzip onetoeight-agent-ms.zip ke dalam folder ini
hermes profile use onetoeight-agent
hermes chat
```

> **Nota:** direktori profil dinamakan `onetoeight-agent`, bukan
> `onetoeight`. Kemas kini arahan yang merujuk laluan profil itu
> dengan sewajarnya.

Untuk kemas kini kemudian: muat turun zip baharu dan unzip ke folder
sementara. Salin fail-fail baharu masuk, tetapi **jangan padam**
folder `memories/` anda dan sesi yang direkodkan. `LOCALE.md` di akar
folder merekodkan binaan asalnya.

### 3: Sembang pertama → orientasi

Pada sembang pertama, agen membuka dengan:

> "Sebelum kita mula -- mahu saya bimbing anda melalui persediaan?
> Ia mengambil masa beberapa minit dan memastikan alat, memori, dan
> minit pagi anda berfungsi seperti yang anda mahu. Atau kita boleh
> langkau dan terus mula."

Katakan ya (atau tanya sahaja *"tolong saya sediakan profil saya"*
pada bila-bila masa). Skill `agent-onboarding` akan berjalan.

### 4: Orientasi (berpagar persetujuan)

Orientasi ini berbentuk perbualan. Agen bertanya satu kumpulan kecil
soalan yang berkaitan pada satu masa dan **berhenti pada setiap
pagar kredential** -- ia tidak pernah meminta kunci atau token dalam
sembang.

Inilah yang diliputinya, mengikut urutan:

| Langkah | Apa yang berlaku | Di mana anda menambahnya |
|---|---|---|
| 1. Identiti | Nama (anda, pelajar, agen), gaya balasan, dan bahasa untuk panduan, pelajaran dan mesej | Disimpan dalam memori profil |
| 2. Profil dan kehidupan | Umur, lokasi, keadaan tempat tinggal, bentuk minggu, 3 minat, matlamat fokus, bulatan persahabatan, penghalang, topik luar batas -- medan yang digunakan agen untuk menyesuaikan Minit Pagi dan pelajaran | Disimpan dalam memori profil |
| 3. Tradisi | Kristian, Universal, atau tradisi sendiri | Disimpan dalam memori profil |
| 4. Pemasangan Piper + suara | Mengesahkan Piper berfungsi, memilih suara, memuat turun model suara | Model suara dalam `piper-voices/` |
| 5. Kunci API Jina | Daftar secara percuma, tambah ke `.env`, agen mengesahkan dengan carian sebenar | `JINA_API_KEY=` dalam `.env` |
| 6. Saluran penyampaian | Kredential bot Telegram atau WhatsApp | `TELEGRAM_BOT_TOKEN=` / `WHATSAPP_*` dalam `.env` |
| 7. Panduan Lapan Esensial | Mengesahkan fail MD pelajaran berada dalam `essentials/01..08/lessons/`, dan berkongsi edisi panduan dalam bahasa pelajar (`essentials/guide-editions.md`) | Fail dalam repo |
| 8. Memori | Mnemosyne disyorkan (tempatan dahulu, tanpa akaun luar) | `hermes memory setup` |
| 9. Jadual Minit Pagi | Pukul berapa, zon waktu apa, hari apa | Dicipta sebagai cron job |
| 10. Jadual Semakan Petang | Pukul berapa, zon waktu apa, hari apa | Dicipta sebagai cron job |
| 11. Jadual Sesi Perancangan | Pukul berapa (default 9 malam), zon waktu apa, hari apa | Dicipta sebagai cron job |
| 12. Token Router (pilihan) | Plugin yang menyempitkan permukaan alat | `plugins.enabled` dalam `config.yaml` |

Pada akhirnya agen menunjukkan ringkasan **Proposed setup** dan
menunggu kelulusan jelas anda sebelum melaksanakan apa-apa.

### 5: Sahkan setiap bahagian

Sebelum Minit Pagi berjadual yang pertama, sahkan setiap komponen:

```bash
# Piper works — test synthesis (paths vary by OS; see below)
echo "The Morning Minute is ready." | piper -m piper-voices/en/en_US/joe/medium/en_US-joe-medium.onnx -f /tmp/piper-test.wav

# Jina works
curl -s -H "Authorization: Bearer jina_x...xxxx" \
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

**Lokasi binari Piper mengikut platform:**

| Platform | Laluan biasa |
|---|---|
| Linux | `/data/.hermes/bin/piper/piper` |
| macOS (Homebrew) | `/opt/homebrew/bin/piper` |
| macOS (manual) | `~/Library/Piper/piper` |
| Windows | `C:/Users/<you>/.openhuman/bin/piper/piper/piper.exe` |
| Windows (pip) | `pip install piper-tts`, kemudian `piper` pada PATH |

Orientasi akan menyiasat Piper dan menemuinya jika ia berada pada
PATH anda. Jika ia dipasang di tempat yang luar biasa, orientasi akan
meminta laluannya.

**Storan model suara** (isi sekali, guna selamanya):

| Suara | Lokal | Laluan Hugging Face |
|---|---|---|
| `en_US-joe-medium` | US lelaki | `rhasspy/piper-voices/resolve/main/en/en_US/joe/medium/en_US-joe-medium.onnx` |
| `en_US-amy-medium` | US perempuan | `rhasspy/piper-voices/resolve/main/en/en_US/amy/medium/en_US-amy-medium.onnx` |
| `en_GB-alan-medium` | UK lelaki | `rhasspy/piper-voices/resolve/main/en/en_GB/alan/medium/en_GB-alan-medium.onnx` |
| `en_GB-jenny_dioco-medium` | UK perempuan | `rhasspy/piper-voices/resolve/main/en/en_GB/jenny_dioco/medium/en_GB-jenny_dioco-medium.onnx` |
| `en_AU-natasha-medium` | AU perempuan | `rhasspy/piper-voices/resolve/main/en/en_AU/natasha/medium/en_AU-natasha-medium.onnx` |

Corak muat turun (contoh -- Joe di Linux):

```bash
mkdir -p ~/.hermes/piper-voices/en/en_US/joe/medium
curl -sL --fail \
  "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/joe/medium/en_US-joe-medium.onnx" \
  -o ~/.hermes/piper-voices/en/en_US/joe/medium/en_US-joe-medium.onnx
curl -sL --fail \
  "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/joe/medium/en_US-joe-medium.onnx.json" \
  -o ~/.hermes/piper-voices/en/en_US/joe/medium/en_US-joe-medium.onnx.json
```

### 6: Larian berjadual yang pertama

Minit Pagi akan menyala pada masa berjadual seterusnya dalam zon waktu
pelajar. Ia menjana audio (Piper), memuat naik ke here.now untuk URL
awam, kemudian menghantar audio itu terus ke Telegram melalui muat
naik multipart -- **bukan** melalui pautan `MEDIA:<url>` (konfigurasi
Cloudflare here.now menyekat bot pengambil fail Telegram).
Semakan Petang menyala pada masa petang berjadual seterusnya.

### 7: Operasi harian

Pelajar tidak berinteraksi dengan agen melalui terminal setiap hari.
Sembang Telegram atau WhatsApp **ialah** permukaan hariannya:

- **Minit Pagi** tiba sebagai nota suara + pelan teks.
- **Semakan Petang** tiba sebagai teks.
- **Sesi Perancangan** tiba sebelum tidur sebagai teks -- agen
  merangka pelan esok (tugasan sekolah, tarikh akhir kerja sekolah,
  esensial minggu itu, satu perkara dunia sebenar), pelajar
  menyuntingnya, dan ia disimpan secara tempatan. Lihat
  `skills/profile/planning-session/`.
- **Balas semakan itu** dengan nota satu baris tentang bagaimana hari
  anda berlalu. Agen menyimpan ringkasan dan menggunakannya sebagai
  panggil balik dalam Minit Pagi esok.
- **Tanya apa-apa soalan pada bila-bila masa.** "Bagaimana rupa
  keyakinan yang teruji sebenarnya?" "Bagaimana saya mencari
  komuniti yang nyata?" Agen membaca panduan dan mengajar.

#### Cara yang lebih mendalam untuk mempelajari esensial (atas permintaan)

Di luar irama harian, pelajar boleh meminta mana-mana daripada
**format yang lebih mendalam** untuk mana-mana esensial.
Kesemuanya dikendalikan oleh skill `essential-deep-dives` (lihat
`skills/profile/essential-deep-dives/`), dan kesemuanya tidak
memerlukan apa-apa selain permintaan:

- **Ringkasan Esensial** -- mata penting satu esensial dalam bahasa
  mudah, serta **nota suara** 3 hingga 5 minit yang dijana oleh agen
  (Piper) dan dimasukkan ke dalam sembang supaya pelajar boleh
  mendengarnya sambil berjalan atau melakukan kerja rumah tangga.
- **Pelajaran Esensial** -- **pelajaran tiga halaman** yang cantik,
  dibina sebagai halaman HTML dan diterbitkan ke akaun **here.now**
  isi rumah. Ia mengajar esensial itu dengan **sumber yang dipetik**
  (diselidik melalui API Jina setiap kali pelajaran memerlukan bahan
  yang tidak dibawa oleh panduan), **petikan penting**, dan **kuiz**
  ringkas yang dijawab oleh pelajar pada halaman itu. Agen
  menghantar pautan itu dalam sembang.
- **Puisi Esensial** -- **puisi lisan** bersajak tentang esensial
  itu, dibaca dengan kuat sebagai nota suara dengan teks di bawahnya
  supaya pelajar boleh membaca sambil mendengar.
- **Lagu Esensial** -- agen menulis puisi asli tentang esensial itu,
  kemudian mengubahnya menjadi lagu sebenar (MP3) melalui
  `google/lyria-3-pro-preview` di OpenRouter (~$0.08 setiap lagu).
  Nota suara dimainkan dalam sembang, teks puisi itu menyusul.
  Sahkan perbelanjaan sebelum menjalankannya.
- **Video Muzik Esensial** -- Lagu di atas, serta papan cerita
  bingkai imej yang dicantumkan dengan audio dan lapisan teks puisi
  sebagai pilihan (~$0.35 kesemuanya untuk lagu + imej papan cerita
  + pemasangan ffmpeg). Diterbitkan sebagai MP4 ke here.now; pautan
  itu masuk ke sembang. Sahkan perbelanjaan sebelum menjalankannya.

Agen membaca panduan sebelum merangka apa-apa daripada ini, bercabang
mengikut tradisi pelajar, dan menyesuaikan mengikut profil pelajar --
peraturan yang sama seperti skill kurikulum.

### 8: Penyelenggaraan

Sekali-sekala:

- `hermes update` -- menarik pustaka skill Hermes standard masuk ke
  dalam profil (skill yang dikurasi tidak pernah ditimpa).
- `git -C ~/.hermes/profiles/onetoeight-agent pull` -- mendapatkan
  penambahbaikan huluan untuk panduan atau skill.
- `cronjob(action="list")` -- mengesahkan kedua-dua cron job masih
  berjadual.

---

## Apa yang anda sediakan dalam `.env`

Profil ini disertakan dengan `.env.example` yang menunjukkan setiap
pemboleh ubah. Inilah yang anda sebenarnya tetapkan.

### Wajib (mana-mana persediaan)

```bash
# Model provider key
OPENAI_API_KEY=...          # or your provider's key name

# Web search (free)
JINA_API_KEY=jina_xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### Wajib untuk penghantaran Telegram

```bash
# Get these from @BotFather in Telegram
TELEGRAM_BOT_TOKEN=1234567890:ABCDefghijklmnopqrstuvwxyz
TELEGRAM_CHAT_ID=123456789
```

> **Nota persediaan Telegram:** selepas mencipta bot anda melalui
> @BotFather, anda **mesti menghantarnya sekurang-kurangnya satu
> mesej** (contohnya `/start`) sebelum agen boleh menghantar kepada
> anda. Bot yang tidak pernah menerima mesej akan gagal menghantar
> secara senyap.

Untuk mencari ID sembang anda: hantar mesej kepada `@userinfobot`
di Telegram dan ia akan membalas dengan ID berangka anda.

### Wajib untuk audio (Minit Pagi)

```bash
# here.now is a site publisher, not a drive. The API key is all you need.
# DRIVE_ID is not used by the audio publish flow — ignore it if you see it.
HERENOW_API_KEY=hn_xxxxxxx
```

> **Nota tentang here.now:** audio dimuat naik melalui API penerbitan
> here.now, yang memberikan URL awam. URL ini dihantar ke Telegram
> melalui muat naik multipart -- ia **tidak** memerlukan DRIVE_ID.
> Jika anda melihat `HERENOW_DRIVE_ID` dalam dokumen atau contoh
> lama, ia legasi dan tidak digunakan oleh aliran penghantaran audio
> semasa.

### Integrasi pilihan

```bash
# Notion
NOTION_API_KEY=...

# GitHub (for tracking, opening issues)
GITHUB_TOKEN=...

# Bluesky (if you publish there)
BLUESKY_HANDLE=...
BLUESKY_APP_PASSWORD=...
```

### Perkara yang BUKAN pemboleh ubah env

- **Laluan model suara** -- disimpan dalam memori profil, bukan env.
  Laluannya khusus kepada mesin.
- **Jadual cron** -- ditetapkan melalui
  `cronjob(action="create", ...)`, disimpan dalam daftar cron,
  bukan env.
- **Laluan binari Piper** -- disimpan dalam memori profil.
- **Mnemosyne** -- tempatan dahulu, tiada kunci diperlukan.

---

## Apa yang ada dalam repo

```
onetoeight-agent/
├── README.md                              ← fail ini
├── SOUL.md                                ← persona dan suara operasi
├── AGENTS.md                              ← prinsip operasi
├── profile.yaml                           ← deskriptor profil
├── config.yaml                            ← konfigurasi masa jalan Hermes
├── .env.example                           ← setiap pemboleh ubah, dengan komen
├── .gitignore
├── LICENSE                                ← MIT
│
├── essentials/                            ← kandungan sumber Lapan Esensial
│   ├── 00-introduction/lessons/
│   │   ├── christian.md                   ← Pendahuluan (edisi Kristian)
│   │   └── universal.md                   ← Pendahuluan (edisi Universal)
│   ├── 01-silence/
│   │   ├── SKILL.md                       ← nota pengajaran agen untuk esensial ini
│   │   ├── lessons/
│   │   │   ├── README.md                 ← skema fail
│   │   │   ├── christian.md               ← Bab 1 (edisi Kristian)
│   │   │   └── universal.md               ← Bab 1 (edisi Universal)
│   │   └── activities/README.md
│   ├── 02-body/        (struktur sama)
│   ├── 03-skills/      (struktur sama)
│   ├── 04-digital-self-defence/
│   ├── 05-community/
│   ├── 06-knowledge/
│   ├── 07-nature/
│   ├── 08-faith/
│   │   ├── lessons/
│   │   │   ├── christian.md               ← Keyakinan yang Teruji + penyesuaian Kristian
│   │   │   └── universal.md               ← Keyakinan yang Teruji + penyesuaian Sekular
│   │   └── activities/README.md
│   ├── 09-conclusion/lessons/{christian,universal}.md
│   ├── 10-before-after/lessons/{christian,universal}.md
│   └── guide-editions.md                  ← panduan dalam talian dalam sepuluh bahasa
│
├── skills/
│   ├── hermes/                            ← skill Hermes yang dikurasi
│   │   ├── agent-onboarding/  ← orientasi
│   │   ├── morning-minute/                ← pelan harian + audio
│   │   ├── hermes-mnemosyne/              ← penyedia memori
│   │   ├── mnemosyne-maintenance/
│   │   └── skill-auditor/
│   └── profile/                       ← skill profil sendiri
│       ├── afternoon-checkin/           ← renungan petang
│       ├── eight-essentials-curriculum/   ← mengajar daripada panduan
│       ├── essential-deep-dives/          ← format ringkasan, pelajaran, puisi
│       └── setup-walkthrough/            ← persediaan Piper, Jina, saluran
│
├── plugins/hermes-token-router/           ← plugin penyempitan alat (pilihan)
├── memories/                              ← benih amalan operasi umum
└── skins/onetoeight.yaml                 ← tema warna
```

> **Skill Hermes standard** (web, terminal, github, creative, dan lain-lain)
> ditarik masuk oleh `hermes update` dan bukan sebahagian daripada
> repo ini. Ia tersenarai dalam pustaka standard, bukan di sini.

---

## Rujukan konfigurasi

### Penyedia model (`config.yaml`)

```yaml
model:
  default: deepseek-v4-flash
  provider: openrouter
fallback_providers:
  - provider: opencode
    model: deepseek-v4-flash
```

Tukar `provider` dan `default` untuk bertukar. OpenRouter ialah
default kerana satu kunci membuka katalog paling luas -- model
percuma, serta model multimodal (imej, audio) -- tanpa menukar
penyedia. Rantaian sandaran berjalan hanya apabila penyedia utama
tidak tersedia.

### Toolset (`config.yaml`)

Setiap toolset CLI **diaktifkan secara default**. Orientasi memandu
pelajar menyemak setiap satu. Untuk mematikannya secara manual:

```bash
hermes --profile onetoeight-agent tools
# Or start with a specific set:
hermes --profile onetoeight-agent chat --toolsets "web,terminal,file,memory"
```

Toolset `tts` mesti kekal aktif untuk Minit Pagi.

### Cron job

Ciptanya melalui orientasi. Untuk pengurusan manual:

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

Lihat `skills/hermes/morning-minute/SKILL.md` untuk kontrak penuh
cron Minit Pagi.

> **Penghantaran cron:** sesi TUI/CLI tiada saluran penghantaran
> langsung. Jika anda mahu dimaklumkan apabila cron menyala, tetapkan
> `deliver="telegram"` (atau `deliver="all"`) semasa mencipta. Jika
> tidak, output disimpan secara tempatan dan boleh dilihat melalui
> `cronjob(action="list")`.

---

## Perangkap biasa

| Gejala | Punca berkemungkinan | Pembetulan |
|---|---|---|
| Piper gagal dimuatkan | Laluan model suara salah, atau belum dimuat turun | Jalankan semula langkah Piper dalam orientasi |
| Audio Minit Pagi senyap atau terpotong | Teks input TTS terpotong | Pastikan fail teks lengkap sebelum sintesis |
| Penghantaran Telegram gagal dengan "chat not found" | Bot belum pernah menerima mesej | Buka Telegram, cari bot anda, hantar `/start` |
| Audio Telegram tidak muncul | Menggunakan `MEDIA:<url>` dengan URL here.now | Gunakan muat naik multipart melalui `sendVoice` (skill mengendalikannya) |
| Cron menyala pada masa yang salah | Kekeliruan UTC | Cron menyimpan UTC. 6 pagi waktu Malaysia = `0 22 * * *`. 6 pagi Sydney = `0 20 * * *` |
| Jadual kata harian tetapi hanya menyala pada hari persekolahan | Format cron salah | `0 6 * * *` = setiap hari. `0 6 * * 1-5` = Isnin–Jumaat |
| Carian Jina tidak memulangkan apa-apa | Kunci tiada dalam `.env` atau salah | Uji dengan `curl -H "Authorization: Bearer ***" "https://s.jina.ai/"` |
| Agen memberi kandungan tradisi yang salah | Tradisi tiada dalam memori | Jalankan semula langkah tradisi dalam orientasi |
| Fail pelajaran tidak dibaca | Suffix `.christian.md` atau `.universal.md` hilang | Semak `ls essentials/<NN>/lessons/` -- nama fail mesti bersuffix dengan betul |

---

## Plugin Token Router (pilihan)

Token Router ialah plugin Hermes pilihan yang **menyempitkan permukaan
alat** yang ditunjukkan kepada agen -- bukan kepada pelajar. Apabila
diaktifkan, agen melihat lebih sedikit alat secara default, yang
boleh mengurangkan penggunaan token dan memastikan agen fokus pada
kerja Lapan Esensial.

Ia **tidak** menyembunyikan ciri daripada pelajar. Pelajar masih
boleh bertanya apa sahaja; router hanya mempengaruhi pilihan
automatik agen.

Aktifkan jika:
- Anda mahu agen kekal fokus pada pengajaran, bukan pada kod atau analisis data.
- Penggunaan token menjadi kebimbangan.

Biarkan tidak aktif jika:
- Pelajar (atau ibu bapa) mahu permukaan alat yang penuh tersedia.

Untuk mengaktifkan: `hermes plugins enable hermes-token-router`
(selepas `hermes profile use onetoeight-agent`).

---

## Lesen

MIT -- lihat `LICENSE`.

Persona OneToEight Agent ialah arketip pembantu asli yang ditulis
untuk projek ini. Kandungan panduan Lapan Esensial berasal daripada
onetoeight *Eight Essentials* Universal Edition V.3.0.0, disertakan
dengan kebenaran untuk digunakan dalam profil ini.
