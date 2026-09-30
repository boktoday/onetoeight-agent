# OneToEight Agent: pangkalahatang-tanaw at daloy ng pagsasaayos

Ang **OneToEight Agent** ay isang personal na AI assistant na
itinayo sa [Hermes Agent](https://hermes-agent.nousresearch.com/docs)
para sa mga kabataang nag-aaral na isabuhay ang **Walong Mahalaga**
sa pang-araw-araw na gawain. Isa itong maamong mentor na
nagpapatakbo ng pang-araw-araw na ritmo ng mga audio plan, check-in
ng pagninilay, at maliliit na hakbang, na itinuturo mula sa gabay
ng Walong Mahalaga na kasama na sa repo.

Ang README na ito ang pangkalahatang-tanaw at ang daloy para
mapagana ang agent mula simula hanggang maging handa. Basahin ito
minsan, pagkatapos sundan ang mga hakbang.

> **Dalawang paraan ng pagsisimula.** Tahakin ang **build path**
> at buuin ang agent nang paisa-isa: isang kakayahan, isang
> kapakinabangan, bawat linggo, may audio na masusundan. O
> i-install ito gamit ang daloy ng pagsasaayos sa ibaba.
>
> **Simulan ang build path: <https://gladtobe.here.now/build-path/>**

> Basahin ito sa: **Filipino** · [English](README.md) · [Bahasa Melayu](README.ms.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [Español](README.es.md) · [中文](README.zh.md) · [한국어](README.ko.md) · [日本語](README.ja.md)

---

## Ano ang produktong ito

Pinakamahusay na natututuhan ng isang kabataan ang Walong Mahalaga
sa **paggawa ng isang maliit na bagay araw-araw** sa loob ng
mga linggo at buwan, hindi sa pagbabasa ng libro. Nariyan ang
OneToEight Agent para tumulong na tumagal ang pang-araw-araw na
ritmong iyon:

- Isang **Minutong Umaga** (Morning Minute) ang dumarating sa
  oras na pinili ng mag-aaral sa kanilang chat (Telegram o
  WhatsApp). Maikling audio plan ito para sa araw, kasama ang
  teksto.
- Isang **Check-in sa Hapon** (Afternoon Check-In) ang dumarating
  sa hapon. Maikling text message ito: kumusta ang araw, ano ang
  susunod, isang tanong na pagninilayan hanggang bukas.
- Isang **Sesyon ng Pagpaplano** (Planning Session) ang dumarating
  bago matulog. Binabalangkas nito ang bukas: mga gawain sa
  paaralan, mga deadline, ang mahalagang pinag-aaralan ngayong
  linggo, isang totoong bagay na gustong gawin. Ang agent ang
  gumagawa ng plano, ang mag-aaral ang nag-e-edit, at naka-save
  ito nang lokal. Walang app, walang account, walang cloud sync.
- Nagtuturo ang agent mula sa **gabay ng Walong Mahalaga** na
  nasa repo (`essentials/01..08/lessons/*.md`), sangay ayon sa
  tradisyong pinili ng mag-aaral.
- Nailathala rin ang gabay sa **sampung wika**, mababasa online o
  maida-download bilang offline pack para gamitin kahit walang
  internet. Tingnan ang `essentials/guide-editions.md`.

Hindi nagbibigay ng lektura ang agent. Hinihila nito palabas ang
karunungan mula sa mag-aaral sa pamamagitan ng mga tanong,
hinahawakan nang malumanay ang ritmo, at tinutulungan silang
magsimula ulit kapag nadapa, nang walang pagsaway.

### Dalawang tradisyon, o ang sarili mo

Pumipili ang bawat mag-aaral ng isa sa onboarding. O sabihin sa
agent ang tradisyon mo at isasama niya iyon. Nananatili ang agent
sa loob ng napiling tradisyon; hindi ito kailanman naghahalo ng
mga tradisyon:

- **Kristiyano**: nakaangkla sa Bibliya. May talata mula sa
  Bibliya ang Minutong Umaga tuwing umaga, binabasa nang natural.
  Binabalangkas ng check-in ang araw sa loob ng buhay na pananampalataya.
- **Universal (sekular)**: iginagalang ang mga tradisyon ng
  karunungan nang walang doktrina. May maikling pagninilay o
  tanong mula sa isang palaisip ang Minutong Umaga. Binabalangkas
  ng check-in ang araw sa loob ng pagninilay, pasasalamat, at
  layunin.

Maaaring palitan ng mag-aaral ang tradisyon sa ibang pagkakataon,
pero mula sa sandaling iyon ay sangay na ang mga aralin.

### Dalawang pagkakasunod-sunod ng paghahatid

Pumipili rin ang bawat mag-aaral kung paano ihahatid ang Walong
Mahalaga:

- **Sekwensyal** (default): dumaan sa mahalagang 1 hanggang 8
  nang sunod-sunod. Ito ang pinaka-magkakaugnay at ito ang ayos
  na pinagdisenyoan ng gabay. Inirerekomenda para sa mga bagong
  mag-aaral.
- **Random**: kumuha ng kahit anong mahalaga sa kahit anong
  araw, itinutugma sa kailangan ng mag-aaral sa araw na iyon
  (pinakamahabang agwat, pinakabagong paghihirap, sigla ng araw).
  Binubuksan ng bawat Minutong Umaga ang isang buod ng kaalaman
  mula sa napiling mahalaga kasama ang isang maliit na gawain.
  Pinakamainam para sa mga mag-aaral na alam na ang kailangan nila.

Sa dalawang paraan, **nasasakop pa rin ang lahat ng walong
mahalaga.** Maaaring magpalit ang mag-aaral mamaya sa pamamagitan
ng pag-update sa `essentials_order` memory key, walang kailangang
bagong onboarding.

### Ang Walong Mahalaga (sa ayos ng pagtuturo ng gabay)

1. **Katahimikan**: maupo nang tahimik, mag-isa kasama ang sariling isip
2. **Katawan**: tulog, pagkain, tubig, galaw, sikat ng araw
3. **Mga Kasanayan**: kapaki-pakinabang na kakayahan sa totoong buhay (magluto, magkumpuni, magtayo, magbudget)
4. **Digital na Pagtatanggol sa Sarili**: privacy, atensyon, literasiya ng pagkakakilanlan
5. **Tunay na Komunidad**: mga taong alam ang pangalan mo
6. **Kaalaman Kahit Walang Wi-Fi**: pag-aari, hindi inuupahan
7. **Kalikasan**: itinakdang oras sa labas, hindi mapag-uusapan
8. **Mga Paniniwalang Nananatili**: sa iyo, at nananatili ito sa ilalim ng presyon

---

## Paano ito gumagana

### Ang pang-araw-araw na ikot

```
06:00  Minutong Umaga      Audio ng Piper + teksto → Telegram o WhatsApp
        ↓
araw   Ginagawa ng mag-aaral ang isang maliit na hakbang
        ↓
17:00  Check-in sa Hapon   Teksto lang → Telegram o WhatsApp
        ↓
21:00  Sesyon ng Pagpaplano Teksto lang → Telegram o WhatsApp
       Gumagawa ng plano ang agent → ine-edit ng mag-aaral → naka-save lokal
        ↓
        Tulog
        ↓
        Ulitin
```

Pinapatibay ng agent ang ikot na ito nang hindi nangungulit.
Malumanay na nagsisimula ulit ang mga nalagpasang araw. Walang
pagsaway. Walang pangangaral.

**Tungkol sa iskedyul:** Ang mga oras sa itaas ay nasa lokal na
timezone ng mag-aaral. Ang cron daemon ay nag-iimbak ng iskedyul sa
**UTC**. Kung pipiliin mo ang 6 am ng Pilipinas (UTC+8), iniimbak
ito ng cron bilang `0 22 * * *` (22:00 UTC). Ang iskedyul ay laging
"ang oras sa timezone mo", ang conversion sa UTC ay awtomatiko.

### Ang trabaho ng agent sa bawat sandali

| Kailan | Ang agent |
|---|---|
| Unang chat sa bagong profile | Nag-aalok ng oryentasyon, maikli, sa sarili nitong boses |
| Sinabi ng mag-aaral na "i-set up mo ako" | Pinapatakbo ang `agent-onboarding` (may pahintulot, sunod-sunod) |
| Nagtanong ang mag-aaral | Binabasa ang kaugnay na `essentials/<NN-name>/lessons/*.md`, binubuod, nagtuturo |
| Sumindi ang Minutong Umaga cron | Gumagawa ng plano para sa araw, pinapatakbo ang Piper, nag-a-upload, naghahatid nang deretso |
| Sumindi ang Check-in cron | Binabasa ang pinakahuling Minutong Umaga, gumagawa ng maikling pagninilay, naghahatid bilang teksto |
| Sumindi ang Sesyon ng Pagpaplano cron | Gumagawa ng plano para sa bukas (gawain sa paaralan, deadline, mahalaga ng linggo, isang totoong bagay), ine-edit ito ng mag-aaral, naka-save lokal |
| Humingi ng mas malalim na aral ang mag-aaral | Ginagamit ang `eight-essentials-curriculum` skill, binabasa ang gabay, nagtuturo mula rito |

### Ang tumatakbo sa background

Tatlong cron job, lahat patay hangga't hindi inaprubahan ng
mag-aaral sa onboarding:

1. **Minutong Umaga**: sumisindi sa napiling oras sa timezone ng
   mag-aaral, araw-araw (o mga araw ng pasok lang, kung ninanais).
   Gumagawa ng audio + teksto at naghahatid sa Telegram o WhatsApp.
2. **Check-in sa Hapon**: sumisindi sa napiling oras sa hapon,
   parehong patakaran sa araw tulad ng Minutong Umaga. Nagpapadala
   ng maikling text message.
3. **Sesyon ng Pagpaplano**: sumisindi bago matulog (default 9 pm),
   parehong patakaran sa araw. Gumagawa ng plano para sa bukas na
   ie-edit ng mag-aaral, tapos naka-save lokal.

Lahat ng tatlo ay **opt-in**, ginagawa lang ng oryentasyon ang mga
ito kapag may malinaw na pagpayag.

### Ang dalawampung pang-araw-araw na tanong

Maliit na koleksyon ng mga madalas gamiting tanong na maaaring
ihain ng isang kabataan sa OneToEight Agent anumang oras. Binabasa
ng agent ang kaugnay na kabanata ng gabay, ginagamit ang nalalaman
na niya tungkol sa mag-aaral, at sumasagot sa kanilang boses, sa
kanilang tradisyon.

Ang punto ay **hindi** pagsagot sa lahat ng dalawampu araw-araw.
Ang punto ay magkaroon ng maliit na hanay ng madalas gamiting
tanong na naglalabas ng mga mahalaga, naghahatak ng pagninilay, at
nagpapalit ng pagiging mausisa tungo sa pang-araw-araw na gawain.
Pumili ng isa o dalawa. Laktawan ang iba. Magpalit-palit sa buong
linggo.

Nakasulat ang mga tanong sa boses ng kabataan. Hindi nagbibigay ng
lektura pabalik ang agent. Nagtatanong ito, nagbibigay ng puwang
para sa sagot, at sinusundan ng isang maliit na hakbang.

Ang buong file ng mga tanong ay nasa
`essentials/00-introduction/lessons/prompts.md`. Binabasa ito ng
agent kapag humingi ang mag-aaral ng "bagay na maiisip," tanong na
pagninilayan, o tulong kapag natigil.

#### Ayon sa paraan

| Paraan | Mga tanong |
|---|---|
| Pagninilay sa sarili | #1, #3, #6, #7, #12, #15, #16, #20 |
| Gawain | #2, #9, #13, #14, #17, #19 |
| Kritikal na pag-iisip | #5, #8, #10, #18 |
| Pang-araw-araw na ritwal | #11, #16, #20 |

#### Ayon sa sigla

| Sigla | Mungkahing tanong |
|---|---|
| Pagod, mababa | #1, #20, #11 |
| Aligaga, mausisa | #5, #10, #14 |
| Natigil o walang gana | #3, #9, #15 |
| Gustong mag-isip | #4, #6, #16, #18 |
| Gustong gumawa | #2, #9, #13, #17, #19 |

#### Ayon sa mahalaga (lumalabas ang bawat mahalaga nang dalawang beses)

| Mahalaga | Mga tanong na tumutuon dito |
|---|---|
| Katahimikan | #1, #7, #9, #12, #16 |
| Katawan | #2, #9, #14, #19 |
| Mga Kasanayan | #8, #13, #14 |
| Digital na Pagtatanggol sa Sarili | #4, #8, #18 |
| Tunay na Komunidad | #6, #15, #17 |
| Kaalaman Kahit Walang Wi-Fi | #3, #6, #8, #10, #11 |
| Kalikasan | #9, #19 |
| Mga Paniniwalang Nananatili | #1, #5, #7, #10, #16, #18 |

#### Mabibigat na tanong (gamitin nang madalang)

Ang mga tanong **#1**, **#5**, **#10**, at **#18** ay mabibigat.
Hindi kailanman sinasandal ng agent ang mga ito. Kailangang
tukuyin ng mag-aaral ang mga ito nang isa-isa. Kung hiniling ng
mag-aaral ang isang mabigat na tanong at hinuhusgahan ng agent na
mali ang araw, maaari itong malumanay na mag-alok ng mas magaan
na kapalit at ipaliwanag kung bakit.

#### Ang dalawampu

| # | Tanong | Paraan | Sigla | Mga Mahalaga |
|---|----------|------|--------|------------|
| 1 | Magtanong ka ng isang bagay na malamang ayaw kong sagutin, pero dapat. | Pagninilay sa sarili | Pagod / mababa | Lahat ng walo (lalo na ang Mga Paniniwalang Nananatili, Katahimikan) |
| 2 | Bigyan mo ako ng 10-minutong gawain na magpapahiya sa akin sa kapaki-pakinabang na paraan. | Gawain | Gustong gumawa | Katawan, Katahimikan, Mga Paniniwalang Nananatili |
| 3 | Ano ang ginawa ko tatlong araw ang nakalipas na hindi ko pa nagagawa muli? Bakit? | Pagninilay sa sarili | Natigil / walang gana | Pagkilala sa sarili, Kaalaman Kahit Walang Wi-Fi |
| 4 | Pumili ka ng isang mahalagang pinakamahina ako. Ano ang pinakamaliit na gawaing magagawa ko ngayon? | Kritikal na pag-iisip | Gustong mag-isip | Lahat ng walo (diagnostiko) |
| 5 | Tutulan mo ang huli kong desisyon. Ano ang sasabihin ng matalinong kritiko? | Kritikal na pag-iisip | Aligaga / mausisa | Kaalaman Kahit Walang Wi-Fi, Mga Paniniwalang Nananatili |
| 6 | Kung kailangan kong turuan ang isang bagong mag-aaral ng isang bagay na natutuhan ko ngayong taon, ano iyon? | Pagninilay sa sarili | Gustong mag-isip | Kaalaman Kahit Walang Wi-Fi, Tunay na Komunidad |
| 7 | Saan sa buhay ko ako nagpapanggap imbes na tunay na gumagawa? Saan ako tunay na gumagawa imbes na nagpapanggap? | Pagninilay sa sarili | Pagod / mababa | Mga Paniniwalang Nananatili, Katahimikan |
| 8 | Ano ang ipinapaubaya ko na ngayon sa iba na dapat ay ako mismo ang nagtatayo? | Kritikal na pag-iisip | Gustong mag-isip | Mga Kasanayan, Digital na Pagtatanggol sa Sarili, Kaalaman Kahit Walang Wi-Fi |
| 9 | Bigyan mo ako ng 30-minutong gawain na walang kailangang telepono at walang ibang tao. | Gawain | Natigil / walang gana | Katawan, Katahimikan, Kalikasan |
| 10 | Ano ang isang paniniwala kong hindi ko maipagtatanggol kapag pinilit? Dapat ko pa bang panatilihin ito? | Kritikal na pag-iisip | Aligaga / mausisa | Mga Paniniwalang Nananatili, Kaalaman Kahit Walang Wi-Fi |
| 11 | Subukin mo ako sa isang bagay na nakalimutan kong alam ko pala. | Pang-araw-araw na ritwal | Pagod / mababa | Kaalaman Kahit Walang Wi-Fi |
| 12 | Itanong mo sa akin ang huling pagkakataong tunay akong nainip, at ano ang napansin ko sa katahimikan. | Pagninilay sa sarili | Natigil / walang gana | Katahimikan, Katawan |
| 13 | Magmungkahi ka ng isang bagay na matatapos ko ngayon na sinimulan ko mahigit isang linggo na ang nakalipas. | Gawain | Gustong gumawa | Mga Kasanayan, Mga Paniniwalang Nananatili |
| 14 | Gabayan mo ako sa isang praktikal na bagay na hindi ko pa alam gawin: pakainin ang sarili, kumpunihin ang gulong, magsulat ng CV, magpalit ng gulong. | Gawain | Aligaga / mausisa | Mga Kasanayan, Katawan |
| 15 | Sino sa buhay ko ang darating sa alas-dos ng madaling araw? Sino ang hindi? Bakit? | Pagninilay sa sarili | Natigil / walang gana | Tunay na Komunidad |
| 16 | Ihambing mo kung paano ko ginugol ang oras ko ngayon kumpara sa sinabi kong gusto ko. Nasaan ang agwat? | Pang-araw-araw na ritwal | Gustong mag-isip | Mga Paniniwalang Nananatili, Katahimikan |
| 17 | Bigyan mo ako ng pambungad na usapan na magagamit ko sa isang taong hindi ko na nakausap nang maayos. | Gawain | Gustong gumawa | Tunay na Komunidad |
| 18 | Kung buburahin ko ang lahat ng app sa telepono ko maliban sa tatlo, alin ang dapat manatili at bakit? | Kritikal na pag-iisip | Gustong mag-isip | Digital na Pagtatanggol sa Sarili, Mga Paniniwalang Nananatili |
| 19 | Ilakad mo ako sa labas ng 15 minuto. Ano ang talagang dapat kong tingnan, pakinggan, mapansin? | Gawain | Gustong gumawa | Kalikasan, Katawan, Katahimikan |
| 20 | Tapusin natin ang araw. Tatlong bagay na nangyari, tatlong bagay na napansin ko, isang bagay na pinasasalamatan ko. | Pang-araw-araw na ritwal | Pagod / mababa | Lahat ng walo (pagsasara ng araw) |

#### Paano ginagamit ng agent ang mga ito

Binabasa ng agent ang
`essentials/00-introduction/lessons/prompts.md` tuwing humihingi
ng tanong ang mag-aaral. Hindi ito **nagdidikit** ng mga tanong sa
mag-aaral. Binabanggit nito ang isa, inaanyayahan ang mag-aaral na
basahin ito, at nagbibigay ng puwang para sa sagot. Hindi ito
nagtatanong ng tatlong sunod-sunod.

Sa **sekwensyal** na pagkakasunod-sunod, kusang nagkukumpol ang mga
tanong sa paligid ng mahalagang pinag-aaralan ng mag-aaral. Sa
**random** na ayos, pinipili ng agent ang tanong na bagay sa
sandali. Nananatiling available ang lahat ng walong mahalaga sa
dalawang paraan.

---

## Mga pang-araw-araw na ritwal

Ito ang mapa sa isang tingin ng lahat ng ritwal na pinapatakbo ng
agent: ano ito, kailan sumisindi, saan dumarating, at saan ito
dokumentado nang detalyado.

| Ritwal | Kailan | Channel | Ano ang nangyayari |
|---|---|---|---|
| **Minutong Umaga** | Araw-araw sa napiling oras ng mag-aaral (default 6 am) | Telegram o WhatsApp, **voice bubble + teksto** | Audio plan para sa araw, nakatutok sa isang maliit na hakbang mula sa kasalukuyang mahalaga. |
| **Check-in sa Hapon** | Araw-araw sa napiling oras ng mag-aaral (default 5 pm) | Telegram o WhatsApp, **teksto lang** | Pagninilay sa kung kumusta ang araw, plano para bukas, isang tanong na pagninilayan sa gabi. |
| **Sesyon ng Pagpaplano** | Araw-araw bago matulog sa napiling oras ng mag-aaral (default 9 pm) | Telegram o WhatsApp, **teksto lang** | Gumagawa ang agent ng plano para bukas (gawain sa paaralan, deadline, mahalaga ng linggo, isang totoong bagay). Ine-edit ito ng mag-aaral. Naka-save lokal. |
| **Buod ng Mahalaga** | Kapag hiniling, anumang oras | Telegram o WhatsApp, **voice message** | 3 hanggang 5 minutong pasalitang buod ng isang mahalaga + maikling listahan ng mahahalagang punto. |
| **Aral sa Mahalaga** | Kapag hiniling, anumang oras | here.now, **link ng HTML page sa chat** | Tatlong-pahinang aral tungkol sa isang mahalaga, may mga siniping sanggunian, mahahalagang quote, at maikling quiz. |
| **Tula ng Mahalaga** | Kapag hiniling, anumang oras | Telegram o WhatsApp, **voice message + teksto** | Rimat na pasalitang tula tungkol sa mahalaga, binabasa kasama ang teksto sa ibaba. |
| **Kanta ng Mahalaga** | Kapag hiniling, anumang oras | Telegram o WhatsApp, **MP3 voice message + teksto** | Nagsusulat ang agent ng tula tungkol sa mahalaga, tapos ginagawang tunay na kanta via Google Lyria 3 sa OpenRouter. Mga ~$0.08 kada kanta, kumpirmahin bago patakbuhin. |
| **Music Video ng Mahalaga** | Kapag hiniling, anumang oras | here.now, **link ng MP4 video sa chat** | Ang kantang nasa itaas, kasama ang storyboard ng mga still na larawan na pinagsama sa audio, opsyonal na overlay ng teksto ng tula. Mga ~$0.35 lahat-lahat, kumpirmahin bago patakbuhin. |

**Ang araw.** Binubuksan ng Minutong Umaga ang araw,
pinapasara ito ng Check-in, at binabalangkas ng Sesyon ng
Pagpaplano ang bukas bago matulog. Ang tatlong format na kapag
hiniling (Buod / Aral / Tula) ay nariyan anumang oras na gustong
matuto ng isang kabataan ng mas malalim kaysa sa kayang sakupin ng
Minutong Umaga sa isang minuto.

**Nasaan ang code.** Bawat hilera ay nakaturo sa isang skill sa
repo:

| Ritwal | Path ng skill |
|---|---|
| Minutong Umaga | `skills/hermes/morning-minute/` |
| Check-in sa Hapon | `skills/profile/afternoon-checkin/` |
| Sesyon ng Pagpaplano | `skills/profile/planning-session/` |
| Buod, Aral, Tula, Kanta, Music Video | `skills/profile/essential-deep-dives/` (ang Kanta at Music Video ay gumagamit ng `skills/creative/openrouter-lyria-music/` at `skills/creative/poem-song-video-studio/`) |

**Pahintulot.** Ang tatlong cron-based na ritwal (Minutong Umaga,
Check-in, Sesyon ng Pagpaplano) ay patay hangga't hindi inaprubahan
ng mag-aaral o magulang sa onboarding. Ang limang format na kapag
hiniling (Buod, Aral, Tula, Kanta, Music Video) ay available agad,
hihilingin lang ng mag-aaral. Ang dalawang bayad na format (Kanta
at Music Video, Lyria 3 + storyboard na larawan) ay nangangailangan
ng kumpirmasyon ng gastos tuwing hihilingin ang mga ito. Tingnan
ang [Ang daloy ng pagsasaayos → Ang tumatakbo sa
background](#ang-tumatakbo-sa-background) para sa eksaktong
opt-in na daloy.

**Mga skill ng Kanta at Music Video.** Ang dalawang bayad na
format ay gumagamit muli ng dalawang existing na skill:

| Format | Batayang skill | Ano ang idinadagdag nito sa `essential-deep-dives` |
|---|---|---|
| **Kanta ng Mahalaga** | `skills/creative/openrouter-lyria-music/` | TULANG lyrics → MP3 audio via Google Lyria 3 (~$0.08/kanta). |
| **Music Video ng Mahalaga** | `skills/creative/poem-song-video-studio/` | KANTA + ~8 storyboard na larawan + ffmpeg → MP4 (~$0.35 lahat). |

Nasa repo na ang dalawang skill na ito kasama ang buong talaan ng
Lyria 3, mga script, at cost guard. Kinakarga ng agent ang batayang
skill kapag hiniling ng mag-aaral ang format.

**Paano i-customise.** Ginagabayan ng agent ang mag-aaral sa
pagpili ng oras, timezone, at patakaran sa araw para sa bawat cron
ritwal sa setup. Maaaring i-pause, i-resume, o alisin ang tatlo
mamaya gamit ang `cronjob(action="...")`. Ang mga format na kapag
hiniling ay kusang pumipili ng tradisyon ng mag-aaral; ang boses
at haba nito ay namamana mula sa napiling Piper voice ng Minutong
Umaga.

---

## Magkano ang pagpapatakbo nito

Ang OneToEight Agent ay **pay-as-you-go**, walang subscription.
Naglo-load ka ng credit sa isang OpenRouter account at kumukuha
doon ang agent.

| Gastos | Halaga | Tala |
|---|---|---|
| **Unang buwan** | **mga $20** | Saklaw ang setup at ang unang buwan ng tunay na paggamit habang nag-aayos pa ang mag-aaral |
| **Pagkatapos** | **$5–$10 kada buwan** | Magaan na pang-araw-araw na gamit sa murang mga modelo |

Umaasa ang profile sa murang mga modelo para sa rutinang gawain:

- **DeepSeek V4 Flash**: default para sa pang-araw-araw na chat at aralin.
- **Google Gemini 3.7 Flash**: mabilis na fallback para sa maiikling gawain.
- **Open-source na mga modelo** (libre o halos libre): para sa pangunahing, mataas na volume na gawain na hindi nangangailangan ng frontier model.

Nag-iiba-iba ang libreng tier buwan-buwan, kaya nagbabago ang
listahan. Tingnan ang live na listahan ng libreng modelo sa
<https://openrouter.ai/openrouter/free>. Ang profile ay default sa
murang opsyon at kumukuha lang ng mas malaking modelo kapag talagang
kailangan ito ng gawain.

---

## Mga tutorial

Mas gusto mo ba ng gagabay na walkthrough? Kinokolekta ng tutorial
hub ang lahat ng setup page sa isang lugar:

- **Ang build path**: pitong pahina na nagtuturo sa pamamagitan ng paggawa: ang agent ay binubuo nang paisa-isa, may audio na masusundan. Simulan sa <https://gladtobe.here.now/build-path/>.
- **Ang onboarding curriculum**: pitong pahina: ang installer course, mula sa unang install hanggang sa agent na nakakabit na sa chat.
- **Ang walkthrough sheets**: ang setup sa isang pahina, sa tatlong wika.

Buksan ang hub sa <https://gladtobe.here.now/hub-tutorials.html>.
Sakop ng daloy sa ibaba ang parehong laman sa tekstong paraan,
hakbang-hakbang.

---

## Ang daloy ng pagsasaayos

### 1: Mga kailangan muna (minsan lang, sa makina)

Kailangan mo:

- **Hermes Agent** na naka-install. Mabilis na check: `hermes --version`. Tingnan ang [install guide](https://hermes-agent.nousresearch.com/docs).
- **Python 3.10 hanggang 3.13** (hindi ang Windows Store shim, kundi tunay na install). `python --version`.
- **Piper TTS.** Gumaganang install. Tingnan ang Hakbang 2 sa ibaba.
- **ffmpeg** para sa WAV → OGG conversion. `ffmpeg -version`.
- **Isang model provider key.** Default ang profile sa `openrouter + deepseek-v4-flash`. Isang key ang nagbubukas ng malaking catalogue ng mga modelo, kasama ang libreng tier at multimodal (larawan, audio) na mga modelo. Mag-sign up nang libre sa <https://openrouter.ai/> at idagdag ang key gamit ang `hermes setup`. Ang OpenCode Go ang fallback.
- **Isang libreng Jina AI API key** para sa web search. Mag-sign up nang libre sa <https://jina.ai/>, walang credit card. Sapat na ang libreng tier para sa pang-araw-araw na gamit ng isang kabataan.
- **Isang Telegram bot** (inirerekomenda) o WhatsApp bridge. Mas madali ang Telegram, tingnan ang Hakbang 4.

### 2: I-unzip ang profile (minsan lang)

Nakuha mo ang profile bilang isang zip file, `onetoeight-agent-tl.zip`.
I-unzip ito sa loob ng `~/.hermes/profiles/` para maging
`~/.hermes/profiles/onetoeight-agent/`, pagkatapos:

```bash
mkdir -p ~/.hermes/profiles
# i-unzip ang onetoeight-agent-tl.zip sa loob ng folder na ito
hermes profile use onetoeight-agent
hermes chat
```

> **Tala:** ang profile directory ay pinangalanang `onetoeight-agent`,
> hindi `onetoeight`. I-update ang mga command na tumutukoy sa
> profile path ayon dito.

Para sa mga update mamaya: i-download ang bagong zip at i-unzip sa
isang pansamantalang folder. Kopyahin ang mga bagong file papasok,
pero **huwag burahin** ang iyong `memories/` folder at mga naitalang
sesyon. Ang `LOCALE.md` sa ugat ng folder ay nagtatala kung saang
bersyon galing ito.

### 3: Unang chat → oryentasyon

Sa unang chat, binubuksan ng agent ang:

> "Bago tayo magsimula, gusto mo bang gabayan kita sa setup? Ilang
> minuto lang ito at mapapagana ang mga tool, memory, at morning
> minute mo sa paraang gusto mo. O laktawan na natin at dumiretso
> na lang."

Sabihin ang oo (o hilingin lang ang *"tulungan mo akong i-set up
ang profile ko"* anumang oras). Tatakbo ang `agent-onboarding`
skill.

### 4: Ang oryentasyon (may pahintulot)

Conversational ang oryentasyon. Nagtatanong ang agent ng isang
maliit na grupo ng magkakaugnay na tanong sa isang pagkakataon at
**humihinto sa bawat credential gate**, hindi ito kailanman
humingi ng key o token sa chat.

Narito ang saklaw nito, sa pagkakasunod-sunod:

| Hakbang | Ano ang nangyayari | Saan mo idadagdag |
|---|---|---|
| 1. Pagkakakilanlan | Mga pangalan (sa iyo, sa mag-aaral, sa agent), estilo ng sagot, at ang wika para sa gabay, aralin at mga mensahe | Naka-save sa profile memory |
| 2. Profile at buhay | Edad, lokasyon, sitwasyon sa tirahan, hugis ng linggo, 3 interes, focus goal, bilog ng pagkakaibigan, hadlang, bawal na paksa | Naka-save sa profile memory |
| 3. Tradisyon | Kristiyano, Universal, o ang sarili mong tradisyon | Naka-save sa profile memory |
| 4. Piper install + boses | Bine-verify na gumagana ang Piper, pumipili ng boses, nagda-download ng voice model | Voice model sa `piper-voices/` |
| 5. Jina API key | Mag-sign up nang libre, idagdag sa `.env`, bine-verify ng agent sa tunay na search | `JINA_API_KEY=` sa `.env` |
| 6. Delivery channel | Telegram o WhatsApp bot credentials | `TELEGRAM_BOT_TOKEN=` / `WHATSAPP_*` sa `.env` |
| 7. Gabay ng Walong Mahalaga | Kinukumpirma na nasa `essentials/01..08/lessons/` ang lesson files, at ibinabahagi ang edisyon ng gabay sa wika ng mag-aaral (`essentials/guide-editions.md`) | Mga file sa repo |
| 8. Memory | Inirerekomenda ang Mnemosyne (lokal, walang external account) | `hermes memory setup` |
| 9. Iskedyul ng Minutong Umaga | Anong oras, anong timezone, anong mga araw | Ginagawa bilang cron job |
| 10. Iskedyul ng Check-in sa Hapon | Anong oras, anong timezone, anong mga araw | Ginagawa bilang cron job |
| 11. Iskedyul ng Sesyon ng Pagpaplano | Anong oras (default 9 pm), anong timezone, anong mga araw | Ginagawa bilang cron job |
| 12. Token Router (opsyonal) | Ang plugin na nagpapaliit ng tool surface | `plugins.enabled` sa `config.yaml` |

Sa dulo, ipapakita ng agent ang buod na **Proposed setup** at
hihintayin ang malinaw mong pagpayag bago ilapat ang anuman.

### 5: I-verify ang bawat bahagi

Bago unang tumakbo ang Minutong Umaga, i-verify ang bawat
komponent:

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

**Mga lokasyon ng Piper binary ayon sa platform:**

| Platform | Karaniwang path |
|---|---|
| Linux | `/data/.hermes/bin/piper/piper` |
| macOS (Homebrew) | `/opt/homebrew/bin/piper` |
| macOS (mano-mano) | `~/Library/Piper/piper` |
| Windows | `C:/Users/<you>/.openhuman/bin/piper/piper/piper.exe` |
| Windows (pip) | `pip install piper-tts`, tapos `piper` sa PATH |

Hinahanap ng oryentasyon ang Piper at makikita ito kung nasa PATH
mo. Kung naka-install sa hindi karaniwang lugar, itatanong ito ng
oryentasyon.

**Saan naka-save ang voice model** (isang beses mong i-download,
gamitin nang pangmatagalan):

| Boses | Lokal | Hugging Face path |
|---|---|---|
| `en_US-joe-medium` | US lalaki | `rhasspy/piper-voices/resolve/main/en/en_US/joe/medium/en_US-joe-medium.onnx` |
| `en_US-amy-medium` | US babae | `rhasspy/piper-voices/resolve/main/en/en_US/amy/medium/en_US-amy-medium.onnx` |
| `en_GB-alan-medium` | UK lalaki | `rhasspy/piper-voices/resolve/main/en/en_GB/alan/medium/en_GB-alan-medium.onnx` |
| `en_GB-jenny_dioco-medium` | UK babae | `rhasspy/piper-voices/resolve/main/en/en_GB/jenny_dioco/medium/en_GB-jenny_dioco-medium.onnx` |
| `en_AU-natasha-medium` | AU babae | `rhasspy/piper-voices/resolve/main/en/en_AU/natasha/medium/en_AU-natasha-medium.onnx` |

Ang pattern ng pag-download (halimbawa, Joe sa Linux):

```bash
mkdir -p ~/.hermes/piper-voices/en/en_US/joe/medium
curl -sL --fail \
  "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/joe/medium/en_US-joe-medium.onnx" \
  -o ~/.hermes/piper-voices/en/en_US/joe/medium/en_US-joe-medium.onnx
curl -sL --fail \
  "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/joe/medium/en_US-joe-medium.onnx.json" \
  -o ~/.hermes/piper-voices/en/en_US/joe/medium/en_US-joe-medium.onnx.json
```

### 6: Ang unang nakatakdang pagtakbo

Sumisindi ang Minutong Umaga sa susunod na nakatakdang oras sa
timezone ng mag-aaral. Gumagawa ito ng audio (Piper), nag-a-upload
sa here.now para sa pampublikong URL, tapos ipinapadala ang audio
nang deretso sa Telegram gamit ang multipart upload, **hindi** sa
pamamagitan ng `MEDIA:<url>` na link (hinaharang ng Cloudflare
configuration ng here.now ang file fetcher ng Telegram). Sumisindi
ang Check-in sa susunod na nakatakdang oras sa hapon.

### 7: Pang-araw-araw na operasyon

Hindi nakikipag-ugnayan ang mag-aaral sa agent sa terminal
araw-araw. Ang Telegram o WhatsApp chat **ang** pang-araw-araw na
surface nito:

- Ang **Minutong Umaga** ay dumarating bilang voice bubble + tekstong plano.
- Ang **Check-in sa Hapon** ay dumarating bilang teksto.
- Ang **Sesyon ng Pagpaplano** ay dumarating bago matulog bilang teksto; binabalangkas ng agent ang plano para bukas (gawain sa paaralan, deadline, mahalaga ng linggo, isang totoong bagay), ine-edit ito ng mag-aaral, at naka-save lokal. Tingnan ang `skills/profile/planning-session/`.
- **Sagutin ang check-in ng hapon** ng isang linyang tala kung kumusta ang araw mo. Itatago ito ng agent at gagamitin bilang callback sa Minutong Umaga bukas.
- **Magtanong anumang oras.** "Ano ba talaga ang mga paniniwalang nananatili?" "Paano ako makakahanap ng tunay na komunidad?" Binabasa ng agent ang gabay at nagtuturo.

#### Mas malalim na pag-aaral (kapag hiniling)

Higit pa sa pang-araw-araw na ritmo, makakahiling ang mag-aaral ng
mas malalim na format tungkol sa kahit anong mahalaga. Lahat ng
ito ay hawak ng `essential-deep-dives` skill (tingnan ang
`skills/profile/essential-deep-dives/`), at lahat ay isang
hiling lang:

- **Buod ng Mahalaga**: ang mga pangunahing punto ng isang
  mahalaga sa simpleng wika, kasama ang 3 hanggang 5 minutong
  **voice message** na ginawa ng agent (Piper) at ipinadala sa
  chat para mapakinggan habang naglalakad o may ginagawa.
- **Aral sa Mahalaga**: magandang **tatlong-pahinang aral**,
  itinayo bilang HTML page at inilathala sa **here.now** account
  ng sambahayan. Itinuturo nito ang mahalaga gamit ang **mga
  siniping sanggunian** (sinasaliksik via Jina API tuwing
  kailangan ng aral ang materyal na wala sa gabay),
  **mahahalagang quote**, at maikling **quiz** na sinasagot ng
  mag-aaral mismo sa pahina. Ipinapadala ng agent ang link sa
  chat.
- **Tula ng Mahalaga**: **pasalitang tula** tungkol sa mahalaga
  na may rima, binabasa bilang voice message kasama ang teksto sa
  ibaba para mabasa ito habang nakikinig.
- **Kanta ng Mahalaga**: nagsusulat ang agent ng orihinal na
  tula tungkol sa mahalaga, tapos ginagawang tunay na kanta (MP3)
  via `google/lyria-3-pro-preview` sa OpenRouter (~$0.08 kada
  kanta). Umiiral ang voice message sa chat, sumusunod ang
  teksto ng tula. Kumpirmahin ang gastos bago patakbuhin.
- **Music Video ng Mahalaga**: ang Kantang nasa itaas, kasama
  ang storyboard ng mga still na larawan na pinagsama sa audio
  at opsyonal na overlay ng teksto ng tula (~$0.35 lahat para sa
  kanta + storyboard na larawan + ffmpeg assembly). Inilalathala
  bilang MP4 sa here.now, ipinapadala ang link sa chat.
  Kumpirmahin ang gastos bago patakbuhin.

Binabasa ng agent ang gabay bago buuin ang lahat ng ito, sangay
ayon sa tradisyon ng mag-aaral, at umaayon sa profile ng
mag-aaral, parehong patakaran sa curriculum skill.

### 8: Pagpapanatili

Paminsan-minsan:

- `hermes update`: hinihila ang standard na Hermes skill
  library papasok sa profile (hindi kailanman nasasapawan ang mga
  curated na skill).
- `git -C ~/.hermes/profiles/onetoeight-agent pull`: hinihila
  ang mga upstream fix para sa gabay o mga skill.
- `cronjob(action="list")`: kinukumpirma na nakatakda pa rin ang dalawang job.

---

## Ang ise-set up mo sa `.env`

Kasama sa profile ang `.env.example` na nagpapakita ng bawat
variable. Narito ang aktwal mong pinupunan.

### Kailangan (sa anumang setup)

```bash
# Model provider key
OPENAI_API_KEY=...          # or your provider's key name

# Web search (free)
JINA_API_KEY=jina_xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### Kailangan para sa paghahatid sa Telegram

```bash
# Get these from @BotFather in Telegram
TELEGRAM_BOT_TOKEN=1234567890:ABCDefghijklmnopqrstuvwxyz
TELEGRAM_CHAT_ID=123456789
```

> **Tala sa Telegram setup:** pagkatapos gumawa ng bot via
> @BotFather, **kailangan mong magpadala muna rito ng kahit isang
> mensahe** (halimbawa `/start`) bago makapagpadala sa iyo ang
> agent. Ang bot na hindi pa nakatanggap ng mensahe ay tahimik na
> mabibigo sa pagpapadala.

Para hanapin ang chat ID mo: padalhan ng mensahe ang
`@userinfobot` sa Telegram at irereply nito ang numeric ID mo.

### Kailangan para sa audio (Minutong Umaga)

```bash
# here.now is a site publisher, not a drive. The API key is all you need.
# DRIVE_ID is not used by the audio publish flow — ignore it if you see it.
HERENOW_API_KEY=hn_xxxxxxx
```

> **Tala sa here.now:** ina-upload ang audio via here.now publish
> API, na nagbibigay ng pampublikong URL. Ipinapadala ang URL na
> iyon sa Telegram sa pamamagitan ng multipart upload, kaya
> **hindi** ito nangangailangan ng DRIVE_ID. Kung makakita ka ng
> `HERENOW_DRIVE_ID` sa mga lumang dokumento o halimbawa,
> legacy iyon at hindi ginagamit ng kasalukuyang audio delivery
> flow.

### Opsyonal na integrations

```bash
# Notion
NOTION_API_KEY=...

# GitHub (for tracking, opening issues)
GITHUB_TOKEN=...

# Bluesky (if you publish there)
BLUESKY_HANDLE=...
BLUESKY_APP_PASSWORD=...
```

### Mga bagay na HINDI env vars

- **Voice model paths**: naka-save sa profile memory, hindi env.
  Machine-specific ang path.
- **Cron schedules**: itinakda via
  `cronjob(action="create", ...)`, naka-save sa cron registry,
  hindi env.
- **Piper binary path**: naka-save sa profile memory.
- **Mnemosyne**: lokal, walang key.

---

## Ano ang nasa repo

```
onetoeight-agent/
├── README.md                              ← itong file
├── SOUL.md                                ← persona at operational voice
├── AGENTS.md                              ← operational principles
├── profile.yaml                           ← profile descriptor
├── config.yaml                            ← Hermes runtime configuration
├── .env.example                           ← every variable, with comments
├── .gitignore
├── LICENSE                                ← MIT
│
├── essentials/                            ← source content ng Walong Mahalaga
│   ├── 00-introduction/lessons/
│   │   ├── christian.md                   ← Panimula (Kristiyanong edisyon)
│   │   └── universal.md                   ← Panimula (Universal na edisyon)
│   ├── 01-silence/
│   │   ├── SKILL.md                       ← teaching notes ng agent para sa mahalagang ito
│   │   ├── lessons/
│   │   │   ├── README.md                 ← file schema
│   │   │   ├── christian.md               ← Kabanata 1 (Kristiyanong edisyon)
│   │   │   └── universal.md               ← Kabanata 1 (Universal na edisyon)
│   │   └── activities/README.md
│   ├── 02-body/        (parehong structure)
│   ├── 03-skills/      (parehong structure)
│   ├── 04-digital-self-defence/
│   ├── 05-community/
│   ├── 06-knowledge/
│   ├── 07-nature/
│   ├── 08-faith/
│   │   ├── lessons/
│   │   │   ├── christian.md               ← Mga Paniniwalang Nananatili + Kristiyanong customisation
│   │   │   └── universal.md               ← Mga Paniniwalang Nananatili + Sekular na customisation
│   │   └── activities/README.md
│   ├── 09-conclusion/lessons/{christian,universal}.md
│   ├── 10-before-after/lessons/{christian,universal}.md
│   └── guide-editions.md                  ← ang online na gabay sa sampung wika
│
├── skills/
│   ├── hermes/                            ← curated Hermes skills
│   │   ├── agent-onboarding/  ← ang oryentasyon
│   │   ├── morning-minute/                ← pang-araw-araw na plano + audio
│   │   ├── hermes-mnemosyne/              ← memory provider
│   │   ├── mnemosyne-maintenance/
│   │   └── skill-auditor/
│   └── profile/                       ← mga skill ng profile mismo
│       ├── afternoon-checkin/           ← pagninilay sa hapon
│       ├── eight-essentials-curriculum/   ← pagtuturo mula sa gabay
│       ├── essential-deep-dives/          ← buod, aral, tula na mga format
│       └── setup-walkthrough/            ← Piper, Jina, channel setup
│
├── plugins/hermes-token-router/           ← opsyonal na tool-narrowing plugin
├── memories/                              ← general operating practice seeds
└── skins/onetoeight.yaml                 ← colour theme
```

> **Standard na Hermes skills** (web, terminal, github, creative,
> atbp.) ay hinihila ng `hermes update` at hindi bahagi ng repo na
> ito. Nakatira sila sa standard library, hindi dito.

---

## Sanggunian ng configuration

### Model providers (`config.yaml`)

```yaml
model:
  default: deepseek-v4-flash
  provider: openrouter
fallback_providers:
  - provider: opencode
    model: deepseek-v4-flash
```

Palitan ang `provider` at `default` para magpalit. Default ang
OpenRouter dahil binubuksan ng isang key ang pinakamalawak na
catalogue: libre at multimodal (larawan, audio) na mga modelo nang
walang paglipat ng provider. Ang fallback chain ay tumatakbo lang
kapag hindi available ang pangunahing provider.

### Toolsets (`config.yaml`)

Ang bawat CLI toolset ay **aktibo by default**. Ginagabayan ng
oryentasyon ang mag-aaral sa pagsusuri sa bawat isa. Para
mano-manong i-disable:

```bash
hermes --profile onetoeight-agent tools
# Or start with a specific set:
hermes --profile onetoeight-agent chat --toolsets "web,terminal,file,memory"
```

Ang `tts` toolset ay dapat manatiling aktibo para sa Minutong
Umaga.

### Cron jobs

Gawin sila via oryentasyon. Para sa mano-manong pamamahala:

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

Tingnan ang `skills/hermes/morning-minute/SKILL.md` para sa buong
kontrata ng Minutong Umaga cron.

> **Cron delivery:** ang TUI/CLI sessions ay walang direktang
> delivery channel. Kung gusto mong maabisuhan kapag sumindi ang
> isang cron, itakda ang `deliver="telegram"` (o `deliver="all"`)
> sa oras ng paggawa. Kung hindi, naka-save lokal ang output at
> makikita via `cronjob(action="list")`.

---

## Mga karaniwang problema

| Sintomas | Malamang na dahilan | Ayos |
|---|---|---|
| Nabibigo ang Piper sa load | Mali ang voice model path, o hindi pa nadownload | Patakbuhin muli ang hakbang ng Piper sa oryentasyon |
| Tahimik o putol ang audio ng Minutong Umaga | Naputol ang input text ng TTS | Tiyakin na kumpleto ang text file bago mag-synthesise |
| Nabibigo ang Telegram delivery na may "chat not found" | Hindi pa nakatanggap ng mensahe ang bot | Buksan ang Telegram, hanapin ang bot mo, magpadala ng `/start` |
| Hindi lumalabas ang Telegram audio | Gumagamit ng `MEDIA:<url>` na may here.now URL | Gumamit ng multipart upload via `sendVoice` (hinahawakan ito ng skill) |
| Sumisindi ang cron sa maling oras | Kalituhan sa UTC | Nag-iimbak ng UTC ang cron. 6 am ng Pilipinas = `0 22 * * *`. 6 am ng Sydney = `0 20 * * *` |
| Nakatakda bilang araw-araw pero sumisindi lang sa school days | Mali ang cron format | `0 6 * * *` = araw-araw. `0 6 * * 1-5` = Lun–Biy |
| Walang bumabalik na resulta ang Jina search | Nawawala o mali ang key sa `.env` | Subukan gamit ang `curl -H "Authorization: Bearer ***" "https://s.jina.ai/"` |
| Nagbibigay ng maling tradisyon na laman ang agent | Hindi nakatakda ang tradisyon sa memory | Patakbuhin muli ang hakbang ng tradisyon sa oryentasyon |
| Hindi mabasa ang lesson files | Nawawalang `.christian.md` o `.universal.md` suffix | Check `ls essentials/<NN>/lessons/`, dapat tama ang suffix ng file names |

---

## Ang Token Router plugin (opsyonal)

Ang Token Router ay isang opsyonal na Hermes plugin na
**nagpapaliit ng tool surface** na nakikita ng agent, hindi ang
mag-aaral. Kapag aktibo, mas kaunting tool ang nakikita ng agent
by default, na makakabawas ng token usage at nagpapanatili sa
agent na nakatutok sa gawain ng Walong Mahalaga.

**Hindi** nito itinatago ang mga feature mula sa mag-aaral.
Makakapagtanong pa rin ng kahit ano ang mag-aaral; ang router ay
nakaaapekto lang sa kusang pinipili ng agent.

I-enable kung:
- Gusto mong manatiling nakatutok ang agent sa pagtuturo, hindi sa code o data analysis.
- Alalahanin ang token usage.

Iwanang naka-off kung:
- Gusto ng mag-aaral (o magulang) na available ang buong tool surface.

Para i-enable: `hermes plugins enable hermes-token-router`
(pagkatapos ng `hermes profile use onetoeight-agent`).

---

## Lisensya

MIT, tingnan ang `LICENSE`.

Ang OneToEight Agent persona ay orihinal na assistant archetype na
isinulat para sa proyektong ito. Ang laman ng gabay ng Walong
Mahalaga ay hinango sa onetoeight *Eight Essentials* Universal
Edition V.3.0.0, kasama sa ilalim ng pahintulot para gamitin sa
loob ng profile na ito.
