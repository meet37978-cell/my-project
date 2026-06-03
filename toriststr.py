import streamlit as st
import matplotlib.pyplot as plt
import folium
from streamlit_folium import st_folium
import random
import time

places = ["Dwarka", "Goa", "Pune", "Rajasthan", "Jammu & Kashmir", "Punjab"]

low_travel = [600, 2200, 2400, 2600, 2800, 3000]
low_hotel = [500, 600, 550, 700, 800, 650]
low_food = [200, 200, 200, 250, 300, 220]

medium_travel = [4000, 4200, 4400, 4600, 4800, 5000]
medium_hotel = [1000, 1100, 1200, 1300, 1400, 1250]
medium_food = [400, 400, 450, 500, 550, 420]

high_travel = [5000, 5200, 5400, 5600, 5800, 6000]
high_hotel = [1200, 1300, 1400, 1500, 1600, 1450]
high_food = [600, 650, 700, 750, 800, 680]

# ---------------- TITLE ----------------

st.title("🌍 Tourist Package System")

# ---------------- SIDEBAR ----------------

st.sidebar.header("📦 Package Selection")

place = st.sidebar.selectbox("Select Place", places)

persons = st.sidebar.number_input(
    "Number of Persons",
    min_value=1,
    value=1
)

days = st.sidebar.number_input(
    "Trip Days (Minimum 4)",
    min_value=4,
    value=4
)

package = st.sidebar.radio(
    "Package Type",
    ["Low", "Medium", "High"]
)


# ---------------- PACKAGE PRICE ----------------

# ---------------- PACKAGE PRICE ----------------

i = places.index(place)

if package == "Low":
    hotel = low_hotel[i]
    food = low_food[i]

elif package == "Medium":
    hotel = medium_hotel[i]
    food = medium_food[i]

else:
    hotel = high_hotel[i]
    food = high_food[i]


# ---------------- TRANSPORT AVAILABLE ----------------

transport_options = {

    "Dwarka": ["Bus", "Train"],

    "Goa": ["Bus", "Train", "Flight"],

    "Pune": ["Bus", "Train", "Flight"],

    "Rajasthan": ["Bus", "Train", "Flight"],

    "Jammu & Kashmir": ["Train", "Flight"],

    "Punjab": ["Bus", "Train", "Flight"]

}

transport = st.sidebar.selectbox(
    "Select Transport",
    transport_options[place]
)


# ---------------- TRANSPORT PRICE ----------------

transport_prices = {

    "Bus": 2,

    "Train": 1.5,

    "Flight": 5
}


# ---------------- DISTANCE ----------------

distance_data = {

    "Dwarka": 450,

    "Goa": 1100,

    "Pune": 650,

    "Rajasthan": 700,

    "Jammu & Kashmir": 1800,

    "Punjab": 1400
}

distance = distance_data[place]


# ---------------- TRANSPORT COST ----------------

transport_cost = int(
    transport_prices[transport]
    * distance
    * persons
)


# ---------------- BILL ----------------

# Travel cost = transport cost only
total_travel = transport_cost

# Hotel cost
total_hotel = hotel * days * persons

# Food cost
total_food = food * days * persons


# ---------------- SUBTOTAL ----------------

subtotal = (
    total_travel
    + total_hotel
    + total_food
)


# ---------------- DISCOUNT ----------------

discount = 0

if persons >= 10 and package in ["Low", "Medium"]:
    discount = subtotal * 0.10

elif persons >= 5 and package == "High":
    discount = subtotal * 0.10


# ---------------- FINAL TOTAL ----------------

final_total = subtotal - discount

# ---------------- SUBMIT ----------------

if "submitted" not in st.session_state:
    st.session_state.submitted = False

if st.sidebar.button("Submit"):
    st.session_state.submitted = True

# ---------------- MAIN ----------------

if st.session_state.submitted:

    TAB1, TAB2, TAB3, TAB4, TAB5, TAB6, TAB7 = st.tabs([
        "ℹ️ Information",
        "🖼️ Gallery",
        "🎥 Videos",
        "📦 Package Details",
        "💰 Bill",
        "📊 Chart",
        "🗺️ Map"
    ])

    # =========================================================
    # TAB 1 INFORMATION
    # =========================================================

    with TAB1:

        if place == "Dwarka":

            st.subheader("ℹ️ About Dwarka")

            st.write("""
            Dwarka is one of the oldest and most sacred cities in India, located in the state of Gujarat. 
            It is situated on the western coast near the Arabian Sea and is famous for the historic 
            Dwarkadhish Temple dedicated to Lord Krishna.

            Dwarka is also known as the “Kingdom of Krishna” because according to Hindu mythology, 
            Lord Krishna ruled here after leaving Mathura. The city is part of the Char Dham pilgrimage 
            and attracts millions of tourists and devotees every year.

            Major attractions in Dwarka include:
            
            • Dwarkadhish Temple  
            • Bet Dwarka  
            • Gomti Ghat  
            • Rukmini Devi Temple  
            • Nageshwar Jyotirlinga  
            • Sudama Setu Bridge  

            The city is well known for its spiritual atmosphere, sea views, temples, and cultural heritage.
            """)

            st.markdown("### 🔗This is more information.")
            

            st.markdown(
                "[🌐 Wikipedia - Dwarka](https://en.wikipedia.org/wiki/Dwarka)"
            )
        elif place == "Goa":
            st.subheader("ℹ️ About Goa")
            st.write("""Goa  is a state on the southwestern coast of India within the Konkan region. It is geographically separated from the Deccan highlands by the Western Ghats. It is bordered by the Indian states of Maharashtra to the north and Karnataka to the east and south, with the Arabian Sea forming its western coastline. It was the capital of the eastern Portuguese empire until 1961. It is India's smallest state by area and fourth-smallest by population. Panaji (Panjim) is the state's capital, while Vasco da Gama is its largest city by population. The state's official language is Konkani, spoken by the majority of its inhabitants.

            """)
            
            st.markdown("### 🔗This is more information.")
            st.markdown(
                "[🌐 Wikipedia - Goa](https://en.wikipedia.org/wiki/Goa)"
            )
        
        elif place == "Pune":
            st.subheader("ℹ️ About Pune")
            st.write("""Pune , previously spelled in English as Poona (the official name until 1978), is a city in the state of Maharashtra in the Deccan Plateau in Western India. It is the administrative headquarters of the Pune district, and of Pune division. In terms of the total amount of land under its jurisdiction, Pune is the largest city in Maharashtra by area, with a geographical area of 516.18km2, though by population it comes in a distant second to Mumbai. According to the 2011 Census of India, Pune has 7.2 million residents in the metropolitan region, making it the seventh-most populous metropolitan area in India. The city of Pune is part of Pune Metropolitan Region. Pune is one of the largest IT hubs in India. It is also one of the most important automobile and manufacturing hubs of India. Pune is often referred to as the "Oxford of the East" because of its educational institutions.It has been ranked "the most liveable city in India" several times.""")

            st.markdown("### 🔗This is more information.")
            st.markdown(
                "[🌐 Wikipedia - Pune](https://en.wikipedia.org/wiki/Pune)"
            ) 
        elif place == "Rajasthan":
            st.subheader("ℹ️ About Rajasthan")
            st.write("""Rajasthan (Hindi: Rājasthāna, pronounced ; lit. 'Land of Kings') is a state in northwestern India. It is the largest Indian state by area and the seventh largest by population. It covers 342,239 square kilometres (132,139 mi2) or 10.4 per cent of India's total geographical area. It is on India's northwestern side, where it comprises most of the wide and inhospitable Thar Desert (also known as the Great Indian Desert) and shares a border with the Pakistani provinces of Punjab to the northwest and Sindh to the west, along the Sutlej-Indus River valley. It is bordered by five other Indian states: Punjab to the north; Haryana and Uttar Pradesh to the northeast; Madhya Pradesh to the southeast; and Gujarat to the southwest. Its geographical location is 23°3' to 30°12' North latitude and 69°30' to 78°17' East longitude, with the Tropic of Cancer passing through its southernmost tip.
            """)

            st.markdown("### 🔗This is more information.")
            st.markdown(
                "[🌐 Wikipedia - Rajasthan](https://en.wikipedia.org/wiki/Rajasthan)"
            ) 
        
        elif place =="Jammu & Kashmir":
            st.subheader("ℹ️ About Jammu & Kashmir")
            st.write("""Jammu and Kashmir (abbr. J&K) is a region administered by India as a union territory and consists of the southern portion of the larger Kashmir region, which has been the subject of a dispute between India and Pakistan since 1947 and between India and China since 1959.
            The Line of Control separates Jammu and Kashmir from the Pakistani-administered territories of Azad Kashmir and Gilgit-Baltistan in the west and north respectively. It lies to the north of the Indian states of Himachal Pradesh and Punjab and to the west of Ladakh which is administered by India as a union territory. Insurgency in Jammu and Kashmir has persisted in protest over autonomy and rights. In 2019, the Jammu and Kashmir Reorganisation Act was passed, reconstituting the former state of Jammu and Kashmir into two union territories: Ladakh in the east and the residuary Jammu and Kashmir in the west.""")

            st.markdown("### 🔗This is more information.")
            st.markdown(
                "[🌐 Wikipedia - Jammu & Kashmir](https://en.wikipedia.org/wiki/Jammu_and_Kashmir_(union_territory))"
            ) 

        elif place =="Punjab":
            st.subheader("ℹ️ About Punjab")
            st.write(""""Punjab  is a state in northwestern India. Forming part of the larger Punjab region of the Indian subcontinent, the state is bordered by the Indian states and union territories of Himachal Pradesh to the north and northeast, Haryana to the south and southeast, Rajasthan to the southwest, Jammu and Kashmir to the north and Chandigarh — which is also its state capital that it shares with the neighbouring state of Haryana — to the east. To the west, it shares an international border with the identically named Pakistani province of Punjab. The state covers an area of 50,362 square kilometres (19,445 square miles), which is 1.53% of India's total geographical area, making it the 19th-largest Indian state by area out of 28 Indian states (20th largest, if Union Territories are considered). With over 27 million inhabitants, Punjab is the 16th-largest Indian state by population, comprising 23 districts. Punjabi, written in the Gurmukhi script, is the most widely spoken and the official language of the state. The main ethnic group are the Punjabis, with Sikhs (57.7%) and Hindus (38.5%) forming the dominant religious groups. Three of the five traditional Punjab rivers — the Sutlej, Beas, and Ravi — flow through the state.
        """)

            st.markdown("### 🔗This is more information.")
            st.markdown(
                "[🌐 Wikipedia - Punjab](https://en.wikipedia.org/wiki/Punjab)"
            )
    # =========================================================
    # TAB 2 GALLERY
    # =========================================================




    with TAB2:
        st.subheader(f"📸 {place} Gallery")

        place_images = {

            "Dwarka": [
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
            ],

            "Goa": [
                
                ("https://avatars.mds.yandex.net/i?id=1a8e2af769400f86f8e42993407b617d052b5fef-10837749-images-thumbs&n=13","Baga Beach"),
                ("https://avatars.mds.yandex.net/i?id=1b8e9d7f2d9665810bd5e7859533e6e7a62b3499-9228595-images-thumbs&n=13","Calangute Beach"),
                ("https://avatars.mds.yandex.net/i?id=9e174276e6835c66e9b90201581eb3178c07ffa3-5670589-images-thumbs&n=13","Anjuna & Vagator Beach"),
                ("https://avatars.mds.yandex.net/i?id=515588570cba7ba319742926819a5982b9b10ebd-9128286-images-thumbs&n=13","Fort Aguada"),
                ("https://avatars.mds.yandex.net/i?id=7f80cfce798963d269b68c48e5738f6e4146a634-4016799-images-thumbs&n=13","Basilica of Bom Jesus"),
                ("https://avatars.mds.yandex.net/i?id=dd66e4591bae7f5a3bc6bfde8a48e0c0058a5813-9831706-images-thumbs&n=13","Se Cathedral"),
                ("https://avatars.mds.yandex.net/i?id=41070aa00fd7d68020906017f66f26a303cb49a9-5212158-images-thumbs&n=13","Fontainhas"),
                ("https://avatars.mds.yandex.net/i?id=8ac7e8c10713f61e375c4e24f8f785de48939fe4-4149382-images-thumbs&n=13","Dudhsagar Falls "),
                ("https://avatars.mds.yandex.net/i?id=2b4969330e986d4cb4cd62b8f15d86b97f2a8edf-3751006-images-thumbs&n=13","Mangueshi Temple"),
                ("https://avatars.mds.yandex.net/i?id=f7bdafa3a1d127529ac72ae2e4d74e11ce877dd0-5101044-images-thumbs&n=13","Goa Fort")

            ],

            "Pune": [
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
            ],

            "Rajasthan": [
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

            ],

            "Jammu & Kashmir": [
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
            ],

            "Punjab": [
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
        }

        if place in place_images:

            cols = st.columns(2)

            for i, img in enumerate(place_images[place]):

                with cols[i % 2]:

                    st.image(
                        img[0],
                        caption=img[1],
                        use_container_width=True
                    )

        else:
            st.write("No images available")

    # =========================================================
    # TAB 3 VIDEOS
    # =========================================================

    with TAB3:

        st.subheader(f"🎥 {place} Videos")

        place_videos = {

            "Dwarka": [
                "https://youtu.be/9e-9uFKI2uw",
                "https://youtu.be/aDFDnXCjeVU?si=B1w0w04LJjdsQyaB",
                "https://youtu.be/1su1lOofkZg?si=k3b3cxuo0EvTSlhP"
            ],

            "Goa": [
                "https://youtu.be/CsUKoBbWmXs?si=lvBQEcdhI9-JNej-",
                "https://youtu.be/2uVOGbl7I10?si=LVyeEySsHBpeqU4G",
                "https://youtu.be/cBbS8Pi0obo?si=Z6d62pUiPQG_k38_"
            ],

            "Pune": [
                "https://youtu.be/_luvEhipVvc?si=XyePbRFm66B8KzUl",
                "https://youtu.be/SCeSlwJxRKU?si=4H08eO0vyiKUBuHh",
                "https://youtu.be/Scxs7L0vhZ4?si=SCLibwaGfrM59dV_"
            ],

            "Rajasthan": [
                "https://youtu.be/72HclT1QVMI?si=pX2jlcO46_KHAfPI",
                "https://youtu.be/Zyrf1saCc4I?si=kUCsv1hNjyaY7yKb",
                "https://youtu.be/tjOKN0r58Es?si=VEEItAxzePPuzPIr"
            ],

            "Jammu & Kashmir": [
                "https://youtu.be/NGibAYSPxtY?si=_xQ1JaKV7OPt5qb3",
                "https://youtu.be/qwcgRARNavs?si=wDHDY3eEVxKxGAlZ",
                "https://youtu.be/MHZpkHqB-U0?si=XePMZY1pLhj8ghil"
            ],

            "Punjab": [
                "https://youtu.be/inMZ4FKA7_k?si=mUz8QpvMM7mOi7rd",
                "https://youtu.be/--cGDHBJoF4?si=ItBTGpHu1ZoclhOY",
                "https://youtu.be/1vrsXxpubFY?si=MOJ3rsA8RcZFXy78"
            ]
        }

        if place in place_videos:

            for video in place_videos[place]:
                st.video(video)

        else:
            st.write("No videos available")
    # =========================================================
    # TAB 4 PACKAGE DETAILS
    # =========================================================

    with TAB4:

        st.subheader("📦 Selected Package")

        col1, col2 = st.columns(2)

        with col1:
            st.info(f"🏕 Place: {place}")
            st.info(f"👥 Persons: {persons}")
            st.info(f"📅 Days: {days}")
            st.info(f"💼 Package Type: {package}")

        with col2:
            st.success(f"🏨 Hotel Cost: Rs. {total_hotel}")
            st.success(f"🍴 Food Cost: Rs. {total_food}")
            st.success(f"🎁 Discount: Rs. {discount}")
            st.success(f"🚍 Transport Cost: Rs. {transport_cost}")

    # =========================================================
    # TAB 5 BILL
    # =========================================================

    with TAB5:

        st.subheader("💰 Final Bill")

        st.write(f"🚌 Total Travel Cost: Rs. {total_travel}")
        st.write(f"🏨 Total Hotel Cost: Rs. {total_hotel}")
        st.write(f"🍴 Total Food Cost: Rs. {total_food}")
        st.write(f"🎁 Discount: Rs. {discount}")

        st.write("---")

        st.header(f"💵 Final Total: Rs. {final_total}")

        if st.button("Booking Confirmed!"):

            st.success("✅ Booking Submitted Successfully!")

            with st.spinner("Booking Processing..."):
                time.sleep(3)

            booking_id = random.randint(1000, 9999)

            st.success("Booking Confirmed!")
            st.info(f"🆔 Booking ID: {booking_id}")
            st.balloons()

    # =========================================================
    # TAB 6 CHART
    # =========================================================

    with TAB6:

        st.subheader("📊 Expense Chart")

        labels = ["Travel", "Hotel", "Food"]
        values = [total_travel, total_hotel, total_food]

        fig, ax = plt.subplots()

        ax.pie(
            values,
            labels=labels,
            autopct="%1.1f%%"
        )

        st.pyplot(fig)

    # =========================================================
    # TAB 7 MAP
    # =========================================================

    with TAB7:

        st.subheader("🗺️ Tour Route Map")

        ahmedabad = [23.0225, 72.5714]

        m = folium.Map(location=ahmedabad, zoom_start=5)

        route = []
        place_names = []


        if place == "Dwarka":

            if package == "Low":

                route = [
                    ahmedabad,
                    [22.3072, 73.1812],
                    [21.1702, 72.8311],
                    [22.2442, 68.9685],
                    ahmedabad
                ]

                place_names = [
                    "Ahmedabad",
                    "Vadodara",
                    "Surat",
                    "Dwarka",
                    "Return"
                ]

            elif package == "Medium":

                route = [
                    ahmedabad,
                    [22.2442, 68.9685],
                    [22.4676, 70.0577],
                    ahmedabad
                ]

                place_names = [
                    "Ahmedabad",
                    "Dwarka",
                    "Jamnagar",
                    "Return"
                ]

            else:

                route = [
                    ahmedabad,
                    [22.2442, 68.9685],
                    [22.2394, 68.9678],
                    ahmedabad
                ]

                place_names = [
                    "Ahmedabad",
                    "Dwarka",
                    "Bet Dwarka",
                    "Return"
                ]

    

        elif place == "Goa":

            if package == "Low":

                route = [
                    ahmedabad,
                    [19.0760, 72.8777],
                    [18.5204, 73.8567],
                    [15.2993, 74.1240],
                    ahmedabad
                ]

                place_names = [
                    "Ahmedabad",
                    "Mumbai",
                    "Pune",
                    "Goa",
                    "Return"
                ]

            elif package == "Medium":

                route = [
                    ahmedabad,
                    [15.2993, 74.1240],
                    [15.5553, 73.7517],
                    [15.5439, 73.7553],
                    ahmedabad
                ]

                place_names = [
                    "Ahmedabad",
                    "Goa",
                    "Baga",
                    "Calangute",
                    "Return"
                ]

            else:

                route = [
                    ahmedabad,
                    [15.5730, 73.7400],
                    [15.4909, 73.8278],
                    ahmedabad
                ]

                place_names = [
                    "Ahmedabad",
                    "Anjuna",
                    "Aguada",
                    "Return"
                ]

        elif place == "Pune":

            route = [
                ahmedabad,
                [19.0760, 72.8777],
                [18.5204, 73.8567],
                ahmedabad
            ]

            place_names = [
                "Ahmedabad",
                "Mumbai",
                "Pune",
                "Return"
            ]



        elif place == "Rajasthan":

            route = [
                ahmedabad,
                [26.9124, 75.7873],
                [24.5854, 73.7125],
                [26.2389, 73.0243],
                ahmedabad
            ]

            place_names = [
                "Ahmedabad",
                "Jaipur",
                "Udaipur",
                "Jodhpur",
                "Return"
            ]


        elif place == "Jammu & Kashmir":

            route = [
                ahmedabad,
                [28.6139, 77.2090],
                [34.0837, 74.7973],
                [34.0484, 74.3805],
                ahmedabad
            ]

            place_names = [
                "Ahmedabad",
                "Delhi",
                "Srinagar",
                "Gulmarg",
                "Return"
            ]


        elif place == "Punjab":

            route = [
                ahmedabad,
                [31.6200, 74.8765],
                [30.7333, 76.7794],
                ahmedabad
            ]

            place_names = [
                "Ahmedabad",
                "Amritsar",
                "Chandigarh",
                "Return"
            ]

    

        icon_data = {
            "Ahmedabad": ("home", "green"),
            "Vadodara": ("cloud", "blue"),
            "Surat": ("shopping-cart", "orange"),
            "Dwarka": ("star", "red"),
            "Jamnagar": ("info-sign", "purple"),
            "Bet Dwarka": ("flag", "darkred"),

            "Mumbai": ("plane", "cadetblue"),
            "Pune": ("education", "darkblue"),
            "Goa": ("glass", "pink"),
            "Baga": ("heart", "red"),
            "Calangute": ("camera", "purple"),
            "Anjuna": ("music", "orange"),
            "Aguada": ("tower", "black"),

            "Jaipur": ("star", "beige"),
            "Udaipur": ("camera", "darkpurple"),
            "Jodhpur": ("tree-deciduous", "darkgreen"),

            "Delhi": ("briefcase", "gray"),
            "Srinagar": ("leaf", "green"),
            "Gulmarg": ("cloud", "lightblue"),

            "Amritsar": ("certificate", "orange"),
            "Chandigarh": ("road", "blue"),

            "Return": ("repeat", "black")
        }



        for j in range(len(route)):

            place_name = place_names[j]

            icon_name, icon_color = icon_data.get(
                place_name,
                ("info-sign", "blue")
            )

            folium.Marker(
                route[j],
                popup=place_name,
                tooltip=place_name,

                icon=folium.Icon(
                    color=icon_color,
                    icon=icon_name,
                    prefix='glyphicon'
                )

            ).add_to(m)

    

        folium.PolyLine(
            route,
            color="blue",
            weight=5
        ).add_to(m)

        st_folium(
            m,
            width=1000,
            height=500
        )
  

else:

    st.info("⬅️ Please Select Package From Sidebar")