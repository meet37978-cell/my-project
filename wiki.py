import streamlit as st
import streamlit.components.v1 as components

x=st.sidebar.title("Wikipedia")
x = st.sidebar.selectbox("Places", ["Dwarka","Goa","Pune","Rajasthan","Jammu & Kashmir","Punjab"])
menu = st.sidebar.radio(
    "Select a page",
    ["Home", "History", "Gallery","Video","audio"]
)

if st.sidebar.button("submit"):

    if x=="Dwarka":
        if menu == "Home":
            st.title("Welcome to Dwarka")
            st.text("""Dwarka is a coastal town and municipality of Devbhumi Dwarka district in the Indian state of Gujarat. It is located on the western shore of the Okhamandal Peninsula on the right bank of the Gomti river at the mouth of the Gulf of Kutch facing the Arabian Sea.

            Dwarka has the Dwarkadhish Temple dedicated to Krishna, which is one of four sacred Hindu pilgrimage sites called the Chardham founded by Adi Shankaracharya at the four corners of the country. The Dwarkadhish Temple was established as a monastic center and forms part of the Dwarka temple complex.[1][2] Dwarka is also one of the seven most ancient religious cities (Sapta Puri) in India.

            Dwarka is part of the "Krishna pilgrimage circuit" which includes Vrindavan, Mathura, Barsana, Gokul, Govardhan, Kurukshetra, Veraval and Puri.[3] It is one of 12 heritage cities across the country selected under the Heritage City Development and Augmentation Yojana (HRIDAY) scheme of the Government of India to develop civic infrastructure.[4]

            The town has a hot, arid climate with a 16-day rainy season. It had a population of 38,873 in 2011. The main festival of Janmashtami is celebrated in Bhadrapada (August–September).""")

        elif menu=="History":
            st.title("History of Dwarka")
            st.text("""Puranic traditions
                    Main article: Dvārakā

                    Dwarika Jagat Mandir (or Dwarkadhish Temple), view from entrance of the town.

                    A painting depicting Krishna's Dwarka, made during Akbar's reign, from the Smithsonian Institution.
                    Dwarka is considered as the first capital of Gujarat.[2] The name literally means gateway.[13] Dwarka has also been referred to throughout its history as "Mokshapuri", "Dwarkamati", and "Dwarkavati".[14] It is mentioned in the ancient epic period of the Mahabharata.[13] According to legend, Krishna settled here after he defeated and killed his uncle Kamsa at Mathura.[15] This mythological account of Krishna's migration to Dwarka from Mathura is closely associated with the culture of Gujarat.[16] Krishna is also said to have reclaimed 12 yojanas or 96 square kilometres (37 sq mi) of land from the sea to create Dwarka.[17]

                    Archaeological findings suggest the original temple Dwarkadhish Temple dedicated to Krishna was built in 200 BCE at the earliest.[18][19] The temple was rebuilt and enlarged in the 15th–16th century.[21][22] The temple is also the location of Dwaraka maţha, also called Sharada Matha/Peeth and "western peeth",[23][note 1] one of the four peeths (Sanskrit: "religious center") established by Adi Shankaracharya. As an important pilgrimage centre for Hindus, Dwarka has several notable temples, including Rukmini Devi Temple, Gomti Ghat, and Bet Dwarka. There is also a lighthouse at the land end point of Dwarka.

                    Archaeology
                    Archaeological investigations at Dwarka, both on shore and offshore in the Arabian Sea, have been performed by the Archaeological Survey of India. The first investigations carried out on land in 1963 revealed many artefacts.[24] Excavations done at two sites on the seaward side of Dwarka brought to light submerged settlements, a large stone-built jetty, and triangular stone anchors with three holes. The settlements are in the form of exterior and interior walls, and fort bastions. From the typological classification of the anchors it is inferred that Dwarka had flourished as a port during the period of the Middle kingdoms of India.[17] Coastal erosion was probably the cause of the destruction of what was an ancient port. Another excavation near Dwarkadhish temple took place which have yielded a shrine dedicated to Vishnu from 9th century CE, furthermore excavation were conducted which yielded a settlement from 1st century BCE another excavation was conducted in the site for the antiquity of the town, have yielded a settlement probably contemporary to Mahabharata dated around 2nd millennium BCE.[17]

                    Dwarka is mentioned in the copper inscription dated 574 CE of Simhaditya, the Maitraka dynasty minister of Vallabhi. He was the son of Varahdas, the king of Dwarka. The nearby Bet Dwarka island is a religious pilgrimage site and an important archaeological site of the Late Harappan period, with one thermolumienescence date of 1570 BCE.[25][26]

                    Early history
                    An epigraphic reference ascribed to Garulaka Simhaditya, the son of Varahdas, the king of Dwarka, is inscribed on a copper plate dated to 574 CE, found in Palitana. The Greek writer of the Periplus of the Erythraean Sea referred to a place called Baraca, which has been interpreted as present-day Dwarka. A reference made in Ptolemy's Geography identified Barake as an island in the Gulf of Kanthils, which has also been inferred to mean Dwarka.[17]

                    One of the four dhams (religious seats), which were founded by Adi Shankaracharya (686–717 CE) at the four corners of the country, was established as a monastic centre and it forms part of the Dwarka temple complex.[1][2]""")
            
    

        elif menu=="Gallery":
            st.title("Gallery")

            images = [

                ("https://avatars.mds.yandex.net/i?id=e778f1fae30d7f0bfd16f06b34d7c16f0c6d56e1-3596236-images-thumbs&n=13","Dwarka Temple"),
                ("https://avatars.mds.yandex.net/i?id=82701d5a52cead9205aaf35732c7ff5cd80125b9-14362031-images-thumbs&n=13","view of Dwarka"),
                ("https://avatars.mds.yandex.net/i?id=9498b3a3d12b08f6071ef5a1333200f31d6b159c-5148463-images-thumbs&n=13","Beyt Dwarka"),
                ("https://avatars.mds.yandex.net/i?id=a3e227f153b444f2b54e67c8bcb3d8478828da80-9181638-images-thumbs&n=13","Gomti Ghat"),
                ("https://avatars.mds.yandex.net/i?id=f81e1c35a4746b8ccb90f723b6620abea94cde25-5269099-images-thumbs&n=13","rukmini temple"),
                ("https://avatars.mds.yandex.net/i?id=2e4071d7ad4fbaddf77707b5b71962593fd2f6e3-11379423-images-thumbs&n=13","rukmini temple"),
                ("https://avatars.mds.yandex.net/i?id=60d3b79d3325cd7b497e60b5dd125272-7020528-images-thumbs&n=13","Nageshwar Jyotirlinga temple"),
                ("https://avatars.mds.yandex.net/i?id=78f586bbf1bcb967163798566c4a7a03fbb3394e-8287363-images-thumbs&n=13","Nageshwar Jyotirlinga "),
                ("https://s7ap1.scene7.com/is/image/incredibleindia/bhadkeshwar-mahadev-temple-dwarka-gujarat-1-attr-hero?qlt=82&ts=1726734778498","bhadkeshwar mahadev temple"),
                ("https://avatars.mds.yandex.net/i?id=f25312ef6195f74f5a0385b3a00d05cf9f3adfb9-10696063-images-thumbs&n=13","shivrajpur beach")
                ]

            cols = st.columns(2)

            for i in range(len(images)):
                with cols[i % 2]:
                    st.image(images[i][0], caption=images[i][1])

        elif menu == "Video":
            st.title("Dwarka Videos")

            videos = [
                "https://youtu.be/9e-9uFKI2uw",
                "https://youtu.be/aDFDnXCjeVU?si=B1w0w04LJjdsQyaB",
                "https://youtu.be/1su1lOofkZg?si=k3b3cxuo0EvTSlhP"

             ]

            for video in videos:
                st.video(video)

        elif menu == "audio":
            st.title("Dwarka Audio")

            song = [
                "https://open.spotify.com/embed/track/3QckBCXKTX2zTPv8Pj9QBN",
                "https://open.spotify.com/embed/track/1UbKet6WRD01GioL3IM0D3",
                "https://open.spotify.com/embed/track/1hlOi9oWLaWScYwCVEBKHG",
            ]

            for audio in song:
                components.iframe(audio, height=80)
        


    elif x=="Goa":
        if menu == "Home":
            st.title("Home information Goa")
            st.text(""" Goa  is a state on the southwestern coast of India within the Konkan region. It is geographically separated from the Deccan highlands by the Western Ghats. It is bordered by the Indian states of Maharashtra to the north and Karnataka to the east and south, with the Arabian Sea forming its western coastline. It was the capital of the eastern Portuguese empire until 1961. It is India's smallest state by area and fourth-smallest by population. Panaji (Panjim) is the state's capital, while Vasco da Gama is its largest city by population. The state's official language is Konkani, spoken by the majority of its inhabitants.

            The Portuguese, who first voyaged to the subcontinent in the early 16th century as merchants, conquered it on request of Timoji shortly thereafter. Goa became an overseas territory of the Portuguese Empire and part of what was then known as Portuguese India, remaining under Portuguese rule for approximately 451 years until its annexation by India in December 1961. The historic city of Margão (Madgaon) still reflects the cultural legacy of colonisation.

            Goa is one of India’s most developed small states and has the second-highest GDP per capita among all Indian states, more than twice the national average GDP per capita. The Eleventh Finance Commission of India named Goa the best-placed state in terms of infrastructure, while India's National Commission on Population ranked it as having the highest quality of life in the country. It ranks highest among Indian states in the Human Development Index. Goa has a robust tourism sector. It has biodiversity, lying near the Western Ghats, a biodiversity hotspo""")
        
        elif menu=="History":
            st.title("Historyhttps of Goa")
            st.text("""Rock art engravings found in Goa are one of the earliest known traces of human life in India. Goa, situated within the Shimoga-Goa Greenstone Belt in the Western Ghats (an area composed of metavolcanics, iron formations, and ferruginous quartzite), yields evidence for Acheulean occupation. Rock art engravings (petroglyphs) are present on laterite platforms and granite boulders in Usgalimal, near the west-flowing Kushavati river, and in Kajur. In Kajur, the rock engravings of animals, tectiforms, and other designs in granite have been associated with what is considered to be a megalithic stone circle, with a round granite stone in the centre. Petroglyphs, cones, stone-axe, and choppers dating to 10,000 years ago have been found in various locations in Goa, including Kazur, Mauxim, and the Mandovi-Zuari basin. Recently, these petroglyphs have been included in the tentative list of UNESCO world heritage sites.

            Evidence of Paleolithic life is visible at Dabolim, Adkon, Shigao, Fatorpa, Arli, Maulinguinim, Diwar, Sanguem, Pilerne, and Aquem-Margaon. Difficulty in carbon dating the laterite rock compounds poses a problem for determining the exact time period.

            Early Goan society underwent radical change when Indo-Aryan and Dravidian migrants amalgamated with the aboriginal locals, forming the base of early Goan culture.

            Early history
            In the 3rd century BC, Goa was part of the Maurya Empire, ruled by the Buddhist emperor, Ashoka of Magadha. Buddhist monks laid the foundation of Buddhism in Goa. Between the 2nd century BC and the 6th century AD, Goa was ruled by the Bhojas of Goa. The Chutus of Karwar also ruled some parts as feudatories of the Satavahanas of Kolhapur (2nd century BC to the 2nd century AD), Western Kshatrapas (around 150 AD), the Abhiras of Western Maharashtra, Bhojas of Goa, and the Konkan Mauryas as feudatories of the Kalachuris.The rule later passed to the Chalukyas of Badami, who controlled it between 578 and 753, and later the Rashtrakutas of Malkhed from 753 to 963. From 765 to 1015, the Southern Silharas of Konkan ruled Goa as the feudatories of the Chalukyas and the Rashtrakutas. Over the next few centuries, Goa was successively ruled by the Kadambas as the feudatories of the Chalukyas of Kalyani. They patronised Jainism in Goa.

            In 1312, Goa came under the governance of the Delhi Sultanate. The kingdom's grip on the region was weak, and by 1370, it was forced to surrender it to Harihara I of the Vijayanagara Empire. The Vijayanagara monarchs held on to the territory until 1469, when it was appropriated by the Bahmani Sultanate. After that dynasty crumbled, the area fell into the hands of the Sultanate of Bijapur, who established as their auxiliary capital the city known under the Portuguese as Velha Goa (or Old Goa)""")

        elif menu=="Gallery":
            st.title("Gallery")

            images = [

                ("https://avatars.mds.yandex.net/i?id=1a8e2af769400f86f8e42993407b617d052b5fef-10837749-images-thumbs&n=13","Baga Beach"),
                ("https://avatars.mds.yandex.net/i?id=1b8e9d7f2d9665810bd5e7859533e6e7a62b3499-9228595-images-thumbs&n=13","Calangute Beach"),
                ("https://avatars.mds.yandex.net/i?id=9e174276e6835c66e9b90201581eb3178c07ffa3-5670589-images-thumbs&n=13","Anjuna & Vagator Beach"),
                ("https://avatars.mds.yandex.net/i?id=515588570cba7ba319742926819a5982b9b10ebd-9128286-images-thumbs&n=13","Fort Aguada"),
                ("https://avatars.mds.yandex.net/i?id=7f80cfce798963d269b68c48e5738f6e4146a634-4016799-images-thumbs&n=13","Basilica of Bom Jesus"),
                ("https://avatars.mds.yandex.net/i?id=dd66e4591bae7f5a3bc6bfde8a48e0c0058a5813-9831706-images-thumbs&n=13","Se Cathedral"),
                ("https://avatars.mds.yandex.net/i?id=41070aa00fd7d68020906017f66f26a303cb49a9-5212158-images-thumbs&n=13","Fontainhas"),
                ("https://avatars.mds.yandex.net/i?id=8ac7e8c10713f61e375c4e24f8f785de48939fe4-4149382-images-thumbs&n=13","Dudhsagar Falls "),
                ("https://avatars.mds.yandex.net/i?id=2b4969330e986d4cb4cd62b8f15d86b97f2a8edf-3751006-images-thumbs&n=13","Mangueshi Temple"),
                ("https://avatars.mds.yandex.net/i?id=f7bdafa3a1d127529ac72ae2e4d74e11ce877dd0-5101044-images-thumbs&n=13","Goa Fort"),
                ]

            cols = st.columns(2)

            for i in range(len(images)):
                with cols[i % 2]:
                    st.image(images[i][0], caption=images[i][1])

        elif menu == "Video":
            st.title("Goa Videos")

            videos = [
                "https://youtu.be/CsUKoBbWmXs?si=lvBQEcdhI9-JNej-",
                "https://youtu.be/2uVOGbl7I10?si=LVyeEySsHBpeqU4G",
                "https://youtu.be/cBbS8Pi0obo?si=Z6d62pUiPQG_k38_"

             ]

            for video in videos:
                st.video(video)
        elif menu == "audio":
            st.title("Goa Audio")

            song = [
                "https://open.spotify.com/embed/track/7oLBAjVbhu5m0wG32xqSwC",  
                "https://open.spotify.com/embed/track/1cTZMwcBJT0Ka3UJPXOeeN",  
                 
            ]

            for audio in song:
                components.iframe(audio, height=80)

    elif x=="Pune":
        if menu=="Home":
                st.title("Pune")
                st.text("""Pune , previously spelled in English as Poona (the official name until 1978), is a city in the state of Maharashtra in the Deccan Plateau in Western India. It is the administrative headquarters of the Pune district, and of Pune division. In terms of the total amount of land under its jurisdiction, Pune is the largest city in Maharashtra by area, with a geographical area of 516.18km2, though by population it comes in a distant second to Mumbai. According to the 2011 Census of India, Pune has 7.2 million residents in the metropolitan region, making it the seventh-most populous metropolitan area in India. The city of Pune is part of Pune Metropolitan Region. Pune is one of the largest IT hubs in India. It is also one of the most important automobile and manufacturing hubs of India. Pune is often referred to as the "Oxford of the East" because of its educational institutions.It has been ranked "the most liveable city in India" several times.

                Pune at different points in time has been ruled by the Rashtrakuta dynasty, Ahmadnagar Sultanate, the Mughals, and the Adil Shahi dynasty. In the 18th century, the city was part of the Maratha Empire, and the seat of the Peshwas, the prime ministers of the Maratha Empire.[28] Pune was seized by the British East India Company in the Third Anglo-Maratha War; it gained municipal status in 1858, the year in which Crown rule began. Many historical landmarks like Shaniwarwada, Shinde Chhatri, and Vishrambaug Wada date to this era. Historical sites from different eras dot the city.

                Pune has historically been a major cultural centre, with important figures like Dnyaneshwar, Shivaji, Tukaram, Baji Rao I, Balaji Baji Rao, Madhavrao I, Nana Fadnavis, Mahadev Govind Ranade, Gopal Krishna Gokhale, Mahatma Jyotirao Phule, Savitribai Phule, Gopal Ganesh Agarkar, Tarabai Shinde, Dhondo Keshav Karve, and Pandita Ramabai doing their life's work in Pune City or in an area that falls in Pune Metropolitan Region. Pune was a major centre of resistance to the British Raj, with people like Gopal Krishna Gokhale and Bal Gangadhar Tilak playing leading roles in struggle for Indian independence in their times.""")

        elif menu=="History":
            st.title("History of Pune")
            st.text("""Early and Medieval Period

                    The circular Nandi mandapa at the Pataleshwar cave temple was built in the Rashtrakuta era (753–982). The Copper plates dated 858 and 868 CE show that by the 9th century an agricultural settlement known as Punnaka existed at the location of modern Pune. These plates indicate that the region was ruled by the Rashtrakuta dynasty. The Pataleshwar rock-cut temple complex was also built during this era.Pune was part of the territory ruled by the Seuna Yadavas of Devagiri from the 9th century to 1327. After that, Pune came under the control of various Muslim sultanates until the late 1600s.

                    The Maratha Empire Pune was part of the jagir (fiefdom) granted by the Nizamshahi (Ahmadnagar Sultanate) to Maloji Bhosale in 1599.Maloji Bhosale passed the Pune jagir to his son Shahaji Bhosale. In 1636, the town was destroyed by Murar Jagdeo, a general from the rival Adil Shahi dynasty.

                    After the Mughal-Nijamshahi war, Shahaji joined Adilshahi due to political circumstances and regained the Pune jagir. At that time, he selected Pune as the residence of his wife Jijabai and young son Shivaji, the future founder of the Maratha Empire.The Lal Mahal residence of Jijabai and Shivaji was completed in 1640. Shivaji spent his early years there. Jijabai is also said to have commissioned the Kasba Ganapati temple. The Ganesha idol there came to be regarded as the presiding deity (Gramadevata) of Pune.
                    
                    Pune changed hands many times between the Mughals and Marathas during the rest of the 1600s.Recognizing Pune’s military importance, Mughal general Shaista Khan and later Emperor Aurangzeb developed the surrounding areas.

                    Pune was recaptured by the Marathas in June 1670, four months before the Battle of Sinhagad, and remained under Maratha control.From 1703 to 1705, near the end of the 27-year Mughal-Maratha Wars, Aurangzeb occupied the town and temporarily renamed it Muhiyabad. After his death, the name reverted to Pune.

                    Peshwa Rule

                    In 1720, Baji Rao I was appointed Peshwa (Prime Minister) of the Maratha Empire by Shahu I.In 1728, Baji Rao moved his base from Saswad to Pune, beginning Pune’s transformation from a kasbah into a major city.

                    He commissioned the construction of Shaniwar Wada on the right bank of the Mutha River. Construction was completed in 1730, marking the beginning of Peshwa dominance in Pune.His son and successor, Nanasaheb, built a lake at Katraj and an underground aqueduct to supply water from the lake to Shaniwar Wada and the city.Remarkably, this aqueduct was still functioning in 2004.""")
            
        elif menu=="Gallery":
            st.title("Gallery")

            images = [
                ("https://avatars.mds.yandex.net/i?id=68d12d8ef38b1a41edd9d32a5a98bd044fb672e1-5310457-images-thumbs&n=13","Lonavala Guided Tour in Private Vehicle"),
                ("https://avatars.mds.yandex.net/i?id=a001ee67c3d442193076a9bd4c37d5c905960334-5655998-images-thumbs&n=13","eher Retreat Day Picnic Ticket"),
                ("https://avatars.mds.yandex.net/i?id=bf7f4f7f868ab9fc0ece0850a3afd56c92094c93-12666658-images-thumbs&n=13","Hill-station & Heritage: Lonavala & Karla Caves"),
                ("https://avatars.mds.yandex.net/i?id=9fe832140ce2a01ace4de394616c80d3c8904709-12474906-images-thumbs&n=13","Sinhagad Fort"),
                ("https://avatars.mds.yandex.net/i?id=296d224215fe12bcf8a4f31bae8cf48012eb410c-5887379-images-thumbs&n=13","Darshan Museum"),
                ("https://dynamic-media-cdn.tripadvisor.com/media/photo-o/05/aa/36/3d/pu-la-deshpande-garden.jpg","Pune-Okayama Friendship Garden"),
                ("https://upload.wikimedia.org/wikipedia/commons/4/4e/Rajgad_Fort_in_Pune%2C_Maharashtra.jpg","Rajgad Fort"),
                ("https://upload.wikimedia.org/wikipedia/commons/6/62/Shrimant_Dagdushet_halwai_ganpati_temple.jpg","Pune Walking Tour with a Punekar"),
                ("https://dynamic-media-cdn.tripadvisor.com/media/photo-o/13/a2/20/65/tamhini-ghat.jpg?w=1200&h=-1&s=1","Tamhini Ghat"),
                ("https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0e/5c/22/a0/img-20170128-140011-hdr.jpg?w=1200","Mahabaleshwar Hill Station")

            ]
            cols = st.columns(2)

            for i in range(len(images)):
                with cols[i % 2]:
                    st.image(images[i][0], caption=images[i][1])    
        elif menu == "Video":
            st.title("Pune Videos")

            videos = [
    
                "https://youtu.be/_luvEhipVvc?si=XyePbRFm66B8KzUl",
                "https://youtu.be/SCeSlwJxRKU?si=4H08eO0vyiKUBuHh",
                "https://youtu.be/Scxs7L0vhZ4?si=SCLibwaGfrM59dV_"
            ]

            for video in videos:
                st.video(video)

        elif menu == "audio":
            st.title("Pune Audio")

            song = [
                "https://open.spotify.com/embed/artist/7BcFJxi62f6cbPyxdTZGll",
                "https://open.spotify.com/embed/track/4ITtnvLQ6SOA8XhiqkLa24",
                "https://open.spotify.com/embed/track/1Sycm4Zt14PQsGJyTM5KF8"
            ]

            for audio in song:
                components.iframe(audio, height=100)

            
    elif x=="Rajasthan":
        if menu=="Home":
            st.title("Rajasthan")
            st.text(""" Rajasthan (Hindi: Rājasthāna, pronounced ; lit. 'Land of Kings') is a state in northwestern India. It is the largest Indian state by area and the seventh largest by population. It covers 342,239 square kilometres (132,139 mi2) or 10.4 per cent of India's total geographical area. It is on India's northwestern side, where it comprises most of the wide and inhospitable Thar Desert (also known as the Great Indian Desert) and shares a border with the Pakistani provinces of Punjab to the northwest and Sindh to the west, along the Sutlej-Indus River valley. It is bordered by five other Indian states: Punjab to the north; Haryana and Uttar Pradesh to the northeast; Madhya Pradesh to the southeast; and Gujarat to the southwest. Its geographical location is 23°3' to 30°12' North latitude and 69°30' to 78°17' East longitude, with the Tropic of Cancer passing through its southernmost tip.

            Its major features include the ruins of the Indus Valley civilisation at Kalibangan and Balathal, the Dilwara Temples, a Jain pilgrimage site at Rajasthan's only hill station, Mount Abu, in the ancient Aravalli mountain range and eastern Rajasthan, the Keoladeo National Park of Bharatpur, a World Heritage Site known for its bird life. Rajasthan is also home to five national tiger reserves, the Ranthambore National Park in Sawai Madhopur, Sariska Tiger Reserve in Alwar, the Mukundra Hills Tiger Reserve in Kota, Ramgarh Vishdhari Tiger reserve and Karauli Dholpur tiger reserve.

            The State of Rajasthan was formed on 30 March 1949 when the states of the Rajputana Agency of the erstwhile British Empire in India were merged into the new Indian Union. Its capital and largest city is Jaipur. Other important cities are Jodhpur, Kota, Bikaner, Ajmer, Bhilwara, Sawai Madhopur, Bharatpur and Udaipur. The economy of Rajasthan is the seventh-largest state economy in India with ₹10.20 lakh crore (US$120 billion) in gross domestic product and a per capita GDP of ₹118,000 (US$1,400). Rajasthan ranks 22nd among Indian states in human development index.]""")

        elif menu=="History":
            st.title("History of Rajasthan")
            st.text(""" Parts of what is now Rajasthan were partly part of the Vedic Civilisation and the Indus Valley civilisation. Kalibangan, in Hanumangarh district, was a major provincial capital of the Indus Valley Civilisation. Topsfield writes that the Rajputs first entered India from the north west in the first millennium A.D. They established kingdoms in western India in the region that is now known as Rajasthan.

            An archaeological excavation at the Balathal site in Udaipur district shows a settlement contemporary with the Harrapan civilisation dating back to 3000–1500 BCE. Stone Age tools dating from 5,000 to 200,000 years were found in Bundi and Bhilwara districts of the state.

            The Minor Rock Edict 3 of Ashoka, found on the platform in front of the Bairat Temple of Viratnagar, Rajasthan.

            The Matsya kingdom of the Vedic civilisation of India is said to roughly correspond to the former state of Jaipur in Rajasthan and included the whole of Alwar with portions of Bharatpur. The capital of Matsya was at Viratanagar (modern Bairat), which is said to have been named after its founder King Virata.

            Bhargava identifies the two districts of Jhunjhunu and Sikar and parts of Jaipur district along with Haryana districts of Mahendragarh and Rewari as part of Vedic state of Brahmavarta. Bhargava also locates the present day Sahibi River as the Vedic Drishadwati River, which along with Saraswati River formed the borders of the Vedic state of Brahmavarta. Manu and Bhrigu narrated the Manusmriti to a congregation of seers in this area. The ashrams of Vedic seers Bhrigu and his son Chayvan Rishi, for whom Chyawanprash was formulated, were near Dhosi Hill, part of which lies in Dhosi village of Jhunjhunu district of Rajasthan and part of which lies in Mahendragarh district of Haryana.

            The Western Kshatrapas (405–35 BCE), the Saka rulers of the western part of India, were successors to the Indo-Scythians and were contemporaneous with the Kushans, who ruled the northern part of the Indian subcontinent. The Indo-Scythians invaded the area of Ujjain and established the Saka era (with their calendar), marking the beginning of the long-lived Saka Western Satraps state.

            The Allahabad Pillar Inscription (also known as the Prayaga Pillar Inscription) of Samudragupta, AD 360, records that the Abhiras were a powerful tribe who ruled over the whole of Rajasthan.

            Classical era

            Gurjara-Pratihara

            Ghateshwara Mahadeva temple at the Baroli Temple Complex. The temples were built between the 10th and 11th centuries by the Gurjara-Pratihara dynasty.

            The Pratiharas ruled for many dynasties in this part of the country; the region was known as Gurjaratra. Up to the 10th century, almost all of North India acknowledged the supremacy of the Imperial Pratiharas, with their seat of power at Kannauj.

            The Gurjara Pratihar Empire acted as a barrier for Arab invaders from the 8th to the 11th century. The chief accomplishment of the Gurjara-Pratihara Empire lies in its successful resistance to foreign invasions from the west, starting in the days of Junaid. Historian R. C. Majumdar says that this was openly acknowledged by the Arab writers. He further notes that historians of India have wondered at the slow progress of Muslim invaders in India, as compared with their rapid advance in other parts of the world. Now there seems little doubt that it was the power of the Pratihara army that effectively barred the progress of the Arabs beyond the confines of Sindh, their only conquest for nearly 300 years.""")

        elif menu=="Gallery":
            st.title("Gallery")

          
            images = [
                ("https://avatars.mds.yandex.net/i?id=a1b5f928cddc48bce61b546c4a7f74ac01c7074f-5234706-images-thumbs&n=13","Hawa Mahal"),
                ("https://i.ytimg.com/vi/z4Qw4UoeYeU/maxresdefault.jpg","Mehrangarh Fort"),
                ("https://img.pac.ru/landmarks/411102/big/4CECDFBE7F0001013E3014EBAB5A3742.jpg","Udaipur City Palace"),
                ("https://avatars.mds.yandex.net/i?id=b4a4500b34f7ec47f040ff1e11ddc8e693074b45-4569751-images-thumbs&n=13","Jaisalmer Fort"),
                ("https://avatars.mds.yandex.net/i?id=31033dd4db11cfc5edaba419206145d1e8d8c867-10273175-images-thumbs&n=13","Amber Palace"),
                ("https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0f/99/ae/7f/images-14-largejpg.jpg?w=700&h=400&s=1","Mehrangarh Fort"),
                ("https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0c/77/15/9a/photo0jpg.jpg?w=500&h=-1&s=1","Lake Pichola"),
                ("https://avatars.mds.yandex.net/i?id=72738a26089980dd15db0e3c1013c39b006fac6b-10093903-images-thumbs&n=13","Jal Mahal"),
                ("https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0d/8e/20/db/photo9jpg.jpg?w=500&h=400&s=1","Sheesh Mahal"),
                ("https://dynamic-media-cdn.tripadvisor.com/media/photo-o/13/96/8a/82/this-is-the-time-when.jpg?w=500&h=400&s=1","The City Palace")


            ]
            
            cols = st.columns(2)

            for i in range(len(images)):
                with cols[i % 2]:
                    st.image(images[i][0], caption=images[i][1])
        elif menu == "Video":
            st.title("Rajasthan Videos")

            videos = [
    
                "https://youtu.be/72HclT1QVMI?si=pX2jlcO46_KHAfPI",
                "https://youtu.be/Zyrf1saCc4I?si=kUCsv1hNjyaY7yKb",
                "https://youtu.be/tjOKN0r58Es?si=VEEItAxzePPuzPIr"
            ]

            for video in videos:
                st.video(video)
        elif menu == "audio":
            song = [
                    "https://open.spotify.com/embed/track/7zrqO3WRNwCfZ80k4Y9VG5" ,
                    "https://open.spotify.com/embed/track/4QSF0d4ENvMXA03ARpMfaP",
                    "https://open.spotify.com/embed/track/0TrsGqtFXMWCrF9pPMICY9"
           
            ]

            for audio in song:
                components.iframe(audio, height=80)
    elif x == "Jammu & Kashmir":
        if menu == "Home":
            st.title("Jammu & Kashmir")
            st.text("""Jammu and Kashmir (abbr. J&K) is a region administered by India as a union territory and consists of the southern portion of the larger Kashmir region, which has been the subject of a dispute between India and Pakistan since 1947 and between India and China since 1959.

            The Line of Control separates Jammu and Kashmir from the Pakistani-administered territories of Azad Kashmir and Gilgit-Baltistan in the west and north respectively. It lies to the north of the Indian states of Himachal Pradesh and Punjab and to the west of Ladakh which is administered by India as a union territory. Insurgency in Jammu and Kashmir has persisted in protest over autonomy and rights. In 2019, the Jammu and Kashmir Reorganisation Act was passed, reconstituting the former state of Jammu and Kashmir into two union territories: Ladakh in the east and the residuary Jammu and Kashmir in the west.

            Srinagar and Jammu jointly serve as the capital of the region, which is divided into two divisions and 20 districts. The area holds substantial mineral deposits, including sapphire, borax, and graphite. Agriculture and services drive the economy, with major contributors being horticulture, handicrafts, and tourism. Apple cultivation is one of the largest industries, employing 3.5 million people and producing 10% of the gross state domestic product. Despite these activities, over 10% of the population lives below the national poverty line.""")

        elif menu == "History":
            st.title("History of Jammu & Kashmir")
            st.text("""JFor the history prior to Indian administration, see Kashmir § History.

                After the Indo-Pakistani war of 1947–1948, three distinct areas of the princely state of Jammu and Kashmir were under Indian control: Muslim-majority Kashmir Valley, Hindu-majority Jammu region, and Buddhist-dominated Ladakh district. These regions were constituted as Jammu and Kashmir state and accorded special status by Article 370 of the Constitution of India, adopted in 1950. In contrast to other states of India, Jammu and Kashmir established its own constitution, flag, and administrative autonomy. In 1954, Article 35A was introduced via a Presidential Order under Article 370, empowering the Jammu and Kashmir Legislature to define permanent residents and bar Indian citizens from other states from purchasing property. From the early 1950s, Jammu and Kashmir used the titles of Prime Minister and Sadr-e-Riyasat for its executive heads, as permitted under Article 370 and formalised in the Delhi Agreement of 1952. The Constituent Assembly, tasked with drafting the constitution and deciding Article 370's future, adopted the constitution of Jammu and Kashmir in 1957 and then dissolved without recommending 370's abrogation, leading to the provision's indefinite continuation.

                In 1953, Sheikh Abdullah, the first Prime Minister of Jammu and Kashmir, was dismissed and jailed by the Indian government over charges of conspiracy, accused of espousing the creation of an independent country. Over the following decades, Article 370 was steadily diluted through presidential orders that extended various provisions of the Indian constitution to the state without full legislative consent, weakening its autonomy. This deepened political disillusionment, particularly in the Kashmir Valley. In 1965, through a Presidential Order, the Bakshi Ghulam Mohammad-led Congress government in Jammu and Kashmir amended the constitution to replace the titles of Prime Minister and Sadr-e-Riyasat with Chief Minister and Governor, aligning them with other Indian states. Abdullah was released in 1968 and, following the Indira–Sheikh Accord of 1975, returned to power as chief minister after a political reconciliation with the central government. After his death in 1982, unrest and violence persisted in the Kashmiri Valley and, following a disputed state election in 1987, an insurgency persisted in protest over autonomy and rights. In the early 1990s, amid the rise of militancy and targeted violence, a mass exodus of Kashmiri Hindus occurred from the Kashmir Valley. Through the 1990s and 2000s, the region witnessed prolonged violence between insurgent groups and Indian security forces.

                While Article 370 had come to be seen as effectively permanent, it historically faced ideological opposition. In the 1950s, Syama Prasad Mookerjee, founder of the Bharatiya Jana Sangh (BJS), opposed Article 370 on grounds that it hindered national integration and created unequal constitutional treatment. In their 2019 Indian general election manifesto, the Bharatiya Janata Party pledged its revocation. After its victory, the Parliament of India passed resolutions to repeal Article 370 in August 2019, and Article 35A was abolished through suspension of the 1954 Presidential Order. At the same time, a reorganisation act was also passed to reconstitute the state into two union territories: the new union territory of Ladakh, with the residual state continuing as the union territory of Jammu and Kashmir. The reorganisation took effect from 31 October 2019. In the days that followed, nearly 4,000 people, including two former Chief Ministers and hundreds of other politicians, were arrested by the Indian authorities in Kashmir; the state was put under a lockdown and communication and internet services were suspended.

                In April 2020, the government notified a domicile law to replace the previous 'permanent residents' scheme. Under the new law, any one that resided in Jammu and Kashmir for 15 years, or studied for seven years and appeared for Class 10 and Class 12 exams, would be deemed to be a 'domicile'. Government officials that served in Jammu and Kashmir for 10 years and their children also become eligible for domicile status.

                On 11 December 2023, the Supreme Court of India unanimously upheld the abrogation of Articles 370 and 35A, while also directing the union government to restore the statehood of Jammu and Kashmir and hold legislative assembly elections no later than September 2024. The assembly election was held from September to October 2024. The alliance led by Jammu & Kashmir National Conference formed the first government of the residual union territory with Omar Abdullah as chief minister.""")

        elif menu == "Gallery":
            st.title("Gallery")
            images = [
                ("https://avatars.mds.yandex.net/i?id=b6d03db7e5b76b308da01f064f960918328102f1-5905964-images-thumbs&n=13","Vaishno Devi Mandir"),
                ("https://avatars.mds.yandex.net/i?id=cfad2dda459e1f2bf53f9356c07b24b5ada3bde3-16418177-images-thumbs&n=13","Indira Gandhi Tulip Garden"),
                ("https://avatars.mds.yandex.net/i?id=2ec5b2dd53ca5fde9034a9e6ab0c2d775c67dacb-10107372-images-thumbs&n=13","Dal Lake"),
                ("https://avatars.mds.yandex.net/i?id=2d108a6dc093be45e11aff4ed5d8b340406cf5e1-5910407-images-thumbs&n=13","Apharwat Peak"),
                ("https://avatars.mds.yandex.net/i?id=d2fc9ba8e5c69434eabc634313e9b314043abd5f-8552056-images-thumbs&n=13","Baisarani Lake"),
                ("https://avatars.mds.yandex.net/i?id=f0cedb51cd2590f1f030bf7b484b193cdb114102-10637411-images-thumbs&n=13","Sonamarg"),
                ("https://avatars.mds.yandex.net/i?id=81267898af27c4a51733b588501a09227400aae5-5364647-images-thumbs&n=13","Vaishno Devi"),
                ("https://i.pinimg.com/originals/15/0f/54/150f54bf441d0787baf648c93b45a8c7.jpg","Betab Valley"),
                ("https://mediaindia.eu/wp-content/uploads/2024/05/Untitled-design-42-1.png","Aru Valley"),
                ("https://i.pinimg.com/originals/0f/bb/05/0fbb05d45c9586a882ecacac90f4b7be.jpg","Nathatop"),
                ("https://media.holidify.com/images/cmsuploads/compressed/pexels-aadil-mehraj-440728798-27379157_20250207194535.jpg","Gurez Valley"),
                ("https://avatars.mds.yandex.net/i?id=365a18163cf05ee174480fee08519d3f084cfadf-4284582-images-thumbs&n=13","Apharwat Peak")
            ]
            cols = st.columns(2)
            for i in range(len(images)):
                with cols[i % 2]:
                    st.image(images[i][0], caption=images[i][1])

        elif menu == "Video":
            st.title("Jammu & Kashmir Videos")
            videos = [
                "https://youtu.be/NGibAYSPxtY?si=_xQ1JaKV7OPt5qb3",
                "https://youtu.be/qwcgRARNavs?si=wDHDY3eEVxKxGAlZ",
                "https://youtu.be/MHZpkHqB-U0?si=XePMZY1pLhj8ghil"
            ]
            for video in videos:
                st.video(video)

        elif menu == "audio":
            st.title("Jammu & Kashmir Audio")

            song = [
                "https://open.spotify.com/embed/track/5orNEFkFG4RP24goF02AuD",
                "https://open.spotify.com/embed/track/6VBhH7CyP56BXjp8VsDFPZ",
                "https://open.spotify.com/embed/track/2Ofatg9oLA8D6c4pD2o3nW"
            ]

            for audio in song:
                components.iframe(audio, height=80)
    elif x == "Punjab":
        if menu == "Home":
            st.title("Punjab")
            st.text("""Punjab  is a state in northwestern India. Forming part of the larger Punjab region of the Indian subcontinent, the state is bordered by the Indian states and union territories of Himachal Pradesh to the north and northeast, Haryana to the south and southeast, Rajasthan to the southwest, Jammu and Kashmir to the north and Chandigarh — which is also its state capital that it shares with the neighbouring state of Haryana — to the east. To the west, it shares an international border with the identically named Pakistani province of Punjab. The state covers an area of 50,362 square kilometres (19,445 square miles), which is 1.53% of India's total geographical area, making it the 19th-largest Indian state by area out of 28 Indian states (20th largest, if Union Territories are considered). With over 27 million inhabitants, Punjab is the 16th-largest Indian state by population, comprising 23 districts. Punjabi, written in the Gurmukhi script, is the most widely spoken and the official language of the state. The main ethnic group are the Punjabis, with Sikhs (57.7%) and Hindus (38.5%) forming the dominant religious groups. Three of the five traditional Punjab rivers — the Sutlej, Beas, and Ravi — flow through the state.

            The history of Punjab has witnessed the migration and settlement of different tribes of people with different cultures and ideas, forming a civilisational melting pot. The ancient Indus Valley Civilisation flourished in the region until its decline around 1900 BCE. Punjab was enriched during the height of the Vedic period, but declined in predominance with the rise of the Mahajanapadas. The region formed the frontier of initial empires during antiquity including Alexander's and the Maurya empires. It was subsequently conquered by the Kushan Empire, Gupta Empire, and then Harsha's Empire. Punjab continued to be settled by nomadic people; including the Huna, Turkic and the Mongols. Punjab came under Muslim rule c. 1000 CE, and was part of the Delhi Sultanate and the Mughal Empire. Sikhism, based on the teachings of Sikh Gurus, emerged between the 15th and 17th centuries. Conflicts between the Mughals and the later Sikh Gurus precipitated a militarisation of the Sikhs, resulting in the formation of a confederacy after the weakening of the Mughal Empire, which competed for control with the larger Durrani Empire. This confederacy was united in 1801 by Maharaja Ranjit Singh, forming the Sikh Empire""")

        elif menu == "History":
            st.title("History of Punjab")
            st.text("""The Punjab region is noted as the site of one of the earliest urban societies, the Indus Valley Civilisation that flourished from about 3000 B.C. and declined rapidly 1,000 years later, following the Indo-Aryan migrations that overran the region in waves between 1500 and 500 B.C. Frequent intertribal wars stimulated the growth of larger groupings ruled by chieftains and kings, who ruled local kingdoms known as Mahajanapadas. The rise of kingdoms and dynasties in Punjab is chronicled in the ancient Hindu epics, particularly the Mahabharata. The epic battles described in the Mahabharata are chronicled as being fought in what is now the state of Haryana and historic Punjab. The Gandharas, Kambojas, Trigartas, Andhra, Pauravas, Bahlikas (Bactrian settlers of the Punjab), Yaudheyas, and others sided with the Kauravas in the great battle fought at Kurukshetra. According to Dr Fauja Singh and Dr. L. M. Joshi: "There is no doubt that the Kambojas, Daradas, Kaikayas, Andhra, Pauravas, Yaudheyas, Malavas, Saindhavas, and Kurus had jointly contributed to the heroic tradition and composite culture of ancient Punjab." The bulk of the Rigveda was composed in the Punjab region between circa 1500 and 1200 BC, while later Vedic scriptures were composed more eastwards, between the Yamuna and Ganges rivers. The historical Vedic religion constituted the religious ideas and practices in Punjab during the Vedic period (1500–500 BCE), centred primarily in the worship of Indra.

            Rigveda is the oldest Hindu text that originated in the Punjab region.

            The earliest known notable local king of this region was known as King Porus, who fought the famous Battle of the Hydaspes against Alexander the Great. His kingdom spanned between rivers Hydaspes (Jhelum) and Acesines (Chenab); Strabo had held the territory to contain almost 300 cities. He (alongside Abisares) had a hostile relationship with the Kingdom of Taxila which was ruled by his extended family. When the armies of Alexander crossed Indus in its eastward migration, probably in Udabhandapura, he was greeted by the then ruler of Taxila, Omphis. Omphis had hoped to force both Porus and Abisares into submission leveraging the might of Alexander's forces and diplomatic missions were mounted, but while Abisares accepted the submission, Porus refused. This led Alexander to seek a face-off with Porus. Thus began the Battle of the Hydaspes in 326 BC; the exact site remains unknown. The battle is thought to have resulted in a decisive Greek victory; however, A. B. Bosworth warns against an uncritical reading of Greek sources who were exaggerative.

            Alexander later founded two cities—Nicaea at the site of victory and Bucephalous at the battleground, in memory of his horse, who died soon after the battle. Later, tetradrachms would be minted depicting Alexander on horseback, armed with a sarissa and attacking a pair of Indians on an elephant. Porus refused to surrender and wandered about atop an elephant, until he was wounded and his force routed. When asked by Alexander how he wished to be treated, Porus replied "Treat me as a king would treat another king". Despite the apparently one-sided results, Alexander was impressed by Porus and chose to not depose him. Not only was his territory reinstated but also expanded with Alexander's forces annexing the territories of Glausaes, who ruled the area northeast of Porus' kingdom.

            After Alexander's death in 323 BCE, Perdiccas became the regent of his empire, and after Perdiccas's murder in 321 BCE, Antipater became the new regent. According to Diodorus, Antipater recognised Porus's authority over the territories along the Indus River. However, Eudemus, who had served as Alexander's satrap in the Punjab region, treacherously killed Porus. The battle is historically significant because it resulted in the syncretism of ancient Greek political and cultural influences to the Indian subcontinent, yielding works such as Greco-Buddhist art, which continued to have an impact for the ensuing centuries. The region was then divided between the Maurya Empire and the Greco-Bactrian Kingdom in 302 B.C.E. Menander I Soter conquered Punjab and made Sagala (present-day Sialkot) the capital of the Indo-Greek Kingdom. Menander is noted for having become a patron and convert to Greco-Buddhism and he is widely regarded as the greatest of the Indo-Greek kings. Greek influence in the region ended around 12 B.C.E. when the Punjab fell under the Sasanians. """)

        elif menu == "Gallery":
            st.title("Gallery")
            images = [
                ("https://avatars.mds.yandex.net/i?id=a550d37564a0b1daf519144797f778bf2a4c750a-5303596-images-thumbs&n=13","Golden Temple"),
                ("https://avatars.mds.yandex.net/i?id=da3ea3c60837b296892aa267df7f9e21-5092559-images-thumbs&n=13","Wagah Border"),
                ("https://avatars.mds.yandex.net/i?id=c934d383d1662a900f43d904a09f599550d5d7d9-4488220-images-thumbs&n=13","Jallianwala Bagh"),
                ("https://avatars.mds.yandex.net/i?id=cde9371244196b5edd50583e86f5d94a38d84f3c-5268598-images-thumbs&n=13","Anandpur Sahib"),
                ("https://dynamic-media-cdn.tripadvisor.com/media/photo-o/11/46/af/45/the-partition-museum.jpg?w=700&h=-1&s=1","The Partition Museum"),
                ("https://dynamic-media-cdn.tripadvisor.com/media/photo-o/09/52/b7/59/akal-takht.jpg?w=700&h=400&s=1","Akal Takht"),
                ("https://avatars.mds.yandex.net/i?id=ddafbf2c9041a55d890f90da6023e796adec9b40-4055686-images-thumbs&n=13","Durgiana Temple"),
                ("https://avatars.mds.yandex.net/i?id=e29393e6f072bf0ea721a51e249d129270c515d8-5283209-images-thumbs&n=13","Gobindgarh Fort"),
                ("https://dynamic-media-cdn.tripadvisor.com/media/photo-o/05/19/5d/50/gurudwara-nanaksar-jagroan.jpg?w=700&h=400&s=1","Gurudwara Nanaksar Jagroan"),
                ("https://dynamic-media-cdn.tripadvisor.com/media/photo-o/10/d3/82/ab/tarn-taran-sahib.jpg?w=700&h=400&s=1","Tarn Taran Sahib"),
                ("https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0c/b7/93/d9/virasat-e-khalsa.jpg?w=700&h=-1&s=1","Virasat E Khalsa"),
    
            ]
            cols = st.columns(2)
            for i in range(len(images)):
                with cols[i % 2]:
                    st.image(images[i][0], caption=images[i][1])

        elif menu == "Video":
            st.title("Punjab Videos")
            videos = [
                "https://youtu.be/inMZ4FKA7_k?si=mUz8QpvMM7mOi7rd",
                "https://youtu.be/--cGDHBJoF4?si=ItBTGpHu1ZoclhOY",
                "https://youtu.be/1vrsXxpubFY?si=MOJ3rsA8RcZFXy78"
            ]
            for video in videos:
                st.video(video)

        elif menu == "audio":
            st.title("Punjab Audio")
            song = [
                "https://open.spotify.com/embed/track/6LiCNxTWT6gDKE4aYZEObC",
                "https://open.spotify.com/embed/track/2erjvSbTPKGalbZZhPgcCL",       
                "https://open.spotify.com/embed/track/0cYohCh24y1aMjJmcS9RBl"     
            ]

            for audio in song:
                components.iframe(audio, height=80)
        

                                