import streamlit as st
import time
import streamlit.components.v1 as components

# Movie list
movie_list = [
    "Chhaava","Saiyaara","RRR","Pushpa","KGF","Pathaan","Mahavatar Narsimha",
    "Bahubali","Laalo","Dhurandhar"
]

# Progress bar
def show_progress():
    bar = st.progress(0)
    for i in range(101):
        time.sleep(0.003)
        bar.progress(i)

def show_radio(key_name):
    return st.radio("Choose part:", ["Part 1", "Part 2"], key=key_name)

# Gallery function
def show_gallery(movie):
    key = movie.lower()
    st.subheader("📸 Gallery")


    images_data = {
        "chhaava": [
                    ("https://avatars.mds.yandex.net/i?id=f9feffb8164b23e2a8524419e3915a2137b824e9-5273869-images-thumbs&n=13", "Chhaava"),
                    ("https://avatars.mds.yandex.net/i?id=c11b6ae24c4beca395b3d77ed1be2b886adbc5d2-3979623-images-thumbs&n=13","Chhaava"),
                    ("https://avatars.mds.yandex.net/i?id=bb6bf73ba33bb32ff2240597571a735e60adf19c-5232244-images-thumbs&n=13","Chhaava"),
                    ("https://avatars.mds.yandex.net/i?id=1a172ccf682a74e6ce180bac4b82237c5696fd59-4570467-images-thumbs&n=13","Chhaava"),
                    ("https://avatars.mds.yandex.net/i?id=e13f4182bbd7073c8c6c52e798ae50ad395f4e5c-4257750-images-thumbs&n=13","Chhaava"),
                    ("https://avatars.mds.yandex.net/i?id=2ac54689e677c4a9aa7b099637507c4be991e3a1-5168030-images-thumbs&n=13","Chhaava"),
        ],
        "saiyaara": [
                    ("https://avatars.mds.yandex.net/i?id=a546c964b5bfde1497e23ed3eb464c1f96aa5eec-10100636-images-thumbs&n=13","Saiyaara"),
                    ("https://avatars.mds.yandex.net/i?id=75195d7c4d53b87832bae8f52cfd67b28f0aa057-15290750-images-thumbs&n=13","Saiyaara"),
                    ("https://avatars.mds.yandex.net/i?id=4e47946dbe12ecb635364fef52ff18cfd5cd2f50-16724419-images-thumbs&n=13","Saiyaara"),
                    ("https://avatars.mds.yandex.net/i?id=1a3ca22b20b0401f557ba3dd0a7dc239cd1927dd-5883245-images-thumbs&n=13","Saiyaara"),
        ],
        "rrr": [
                    ("https://avatars.mds.yandex.net/i?id=776cb57580d5738b196cd38ad1fc82089d4137c7-12569476-images-thumbs&n=13","RRR"),
                    ("https://avatars.mds.yandex.net/i?id=1e1af03926b24c29de87ab8f2d7d7ab0a335eb1f-5248286-images-thumbs&n=13","RRR"),
                    ("https://avatars.mds.yandex.net/i?id=73196ad1608e143b9d8cc61c3761e9bd08bf46de-8186099-images-thumbs&n=13","RRR"),
                    ("https://avatars.mds.yandex.net/i?id=ef0f46fda082179f3d8a9e89c302767327a1b2e6-5246363-images-thumbs&n=13","RRR"),
                    ("https://avatars.mds.yandex.net/i?id=c647c3f866bd5b78e749df71a3fa4156f6719f91-9182192-images-thumbs&n=13","RRR"),
                    ("https://avatars.mds.yandex.net/i?id=c78f637bb6967a2e5a54432e0bbae646cad3c679-12608033-images-thumbs&n=13","RRR"),
        ],
        "pathaan": [
    
    
            ("https://avatars.mds.yandex.net/i?id=0b42323b3de78a3cf4cfc2b7a7e0d6db0c1226a8-8187817-images-thumbs&n=13","Pathaan"),
            ("https://avatars.mds.yandex.net/i?id=894f0d3cfd533347510e9a9d84fd9c88d1c267c2-8500949-images-thumbs&n=13","Pathaan"),
            ("https://avatars.mds.yandex.net/i?id=d6fdfba499b5ff1abc2e11c455b7d0923f7d4b93-5869158-images-thumbs&n=13","Pathaan"),
            ("https://avatars.mds.yandex.net/i?id=d22e41edaac07757ba8734230c1a14f65ac945fe-9052390-images-thumbs&n=13","Pathaan"),
            ("https://avatars.mds.yandex.net/i?id=09f705d59e00b13d57614bda4d9e68a83d0504a9-9589172-images-thumbs&n=13","Pathaan"),
            ("https://avatars.mds.yandex.net/i?id=4d961e4649da6eb60f950ca5940745fa6ad0033e-5221151-images-thumbs&n=13","Pathaan"),

        ],
        "mahavatar narsimha":[
            
            ("https://avatars.mds.yandex.net/i?id=95f055fd05f80d233d05f8f332759894e7b36093-10385082-images-thumbs&n=13","Mahavatar Narsimha"),
            ("https://avatars.mds.yandex.net/i?id=4b8afd40663655717e5c167baad749fcf0bbf12a-10450775-images-thumbs&n=13","Mahavatar Narsimha"),
            ("https://avatars.mds.yandex.net/i?id=3e93ce8814f9f39bfa21371f99459ec6e0062ee6-5509039-images-thumbs&n=13","Mahavatar Narsimha"),
            ("https://avatars.mds.yandex.net/i?id=f7f504cad5b098d7922c563d23cfac13f09829bd-5341800-images-thumbs&n=13","Mahavatar Narsimha"),
            ("https://avatars.mds.yandex.net/i?id=4e19c58dd53d1ba62283a74d324e877fbfc42fc7-12720093-images-thumbs&n=13","Mahavatar Narsimha"),
            ("https://avatars.mds.yandex.net/i?id=4b842075f22189d813b55d9f43c7e074862d53d8-16330135-images-thumbs&n=13","Mahavatar Narsimha"),
        ],
        "laalo":[
            ("https://avatars.mds.yandex.net/i?id=502034e143328b6b44fd663ec2fb14e631e5e091-7459916-images-thumbs&n=13","Laalo"),
            ("https://avatars.mds.yandex.net/i?id=55a92c8964de1692125073a4a0634073c2938c17-3529463-images-thumbs&n=13","Laalo"),
            ("https://avatars.mds.yandex.net/i?id=4c4972d729c2bae2f28ce58377ad84dc68c7a295-4613271-images-thumbs&n=13","Laalo"),
            ("https://avatars.mds.yandex.net/i?id=2f0160f57c842b453e1cbfd62d7e6f49a4fd60c1-4599933-images-thumbs&n=13","Laalo"),
            ("https://avatars.mds.yandex.net/i?id=7f1477e2c835654e1bcafcf677b7feb7584ef5f3-5616093-images-thumbs&n=13","Laalo"),
            ("https://avatars.mds.yandex.net/i?id=fe7588fd240015751d8b2b713f1c362732a41261-9833405-images-thumbs&n=13","Laalo"),
        ],
    }

    images = []

    if key == "pushpa":
        ch = show_radio("pushpa_part")
        if ch == "Part 1":
            images = [
                ("https://avatars.mds.yandex.net/i?id=47593ca31bc8c2d24903db8962fbe8b5db7c2b3e-9193117-images-thumbs&n=13", "Pushpa 1"),
                ("https://avatars.mds.yandex.net/i?id=3d7054075e4dd9af5bedd10c1b3269610f34bc2b-8439163-images-thumbs&n=13", "Pushpa 1"),
                ("https://avatars.mds.yandex.net/i?id=11f5c765234909997a37a852c84b355425dd88e2-9097048-images-thumbs&n=13", "Pushpa 1"),
                ("https://avatars.mds.yandex.net/i?id=01cffa0c17f93d2963cae1e679073f7d4f8d62e2-4146380-images-thumbs&n=13", "Pushpa 1"),
                ("https://avatars.mds.yandex.net/i?id=8a04ebc3960be61d4fc91cad94468b65b7fd2389-9181093-images-thumbs&n=13", "Pushpa 1"),
                ("https://avatars.mds.yandex.net/i?id=cbd0ac335c77081e5ab7127995b9db88bd4cab20-5306350-images-thumbs&n=13", "Pushpa 1"),    
            ]
        else:
            images = [
                ("https://avatars.mds.yandex.net/i?id=4638e798dcb2eb169e907157f59719d1b974a0d1-5234542-images-thumbs&n=13"  , "Pushpa 2"),
                ("https://avatars.mds.yandex.net/i?id=8a04ebc3960be61d4fc91cad94468b65b7fd2389-9181093-images-thumbs&n=13", "Pushpa 2"),
                ("https://avatars.mds.yandex.net/i?id=e9664f654e801944893638a086b4532ef3c8926e-8497203-images-thumbs&n=13", "Pushpa 2"),
                ("https://avatars.mds.yandex.net/i?id=1a7693832c9392139d91f10575b1fde62efaa04e-5518476-images-thumbs&n=13", "Pushpa 2"),
                ("https://avatars.mds.yandex.net/i?id=43bc5378af1bca3b326c2affd1861c097685bb0c-5621662-images-thumbs&n=13", "Pushpa 2"),
                ("https://avatars.mds.yandex.net/i?id=f60f5bca8c3bfcc2e5df25b5331db3c6550c15df-5450477-images-thumbs&n=13", "Pushpa 2"),
            ]

    # KGF
    elif key == "kgf":
        ch = show_radio("kgf_part")
        if ch == "Part 1":
            images = [
                ("https://avatars.mds.yandex.net/i?id=ac05cb45212cb3bac1562faae967021dafbc6a1d-16305219-images-thumbs&n=13", "KGF 1"),
                ("https://avatars.mds.yandex.net/i?id=95206b8f5624a500f96230748ead4820b35958f5-5022452-images-thumbs&n=13", "KGF 1"),
                ("https://avatars.mds.yandex.net/i?id=37d6101149c900a6f083658c7072f8b798de9f66-5220694-images-thumbs&n=13", "KGF 1"),
                ("https://avatars.mds.yandex.net/i?id=1d9d10bcc7d0a71173e25c6139a96d7d06fcb50b-10114683-images-thumbs&n=13", "KGF 1"),
                ("https://avatars.mds.yandex.net/i?id=c43ad58c82328513271a3e3c177054f82d1c03ac-8187817-images-thumbs&n=13", "KGF 1"),
                ("https://avatars.mds.yandex.net/i?id=1913c717aa420be0c3b23139301ce5938ba0e7bc-12421657-images-thumbs&n=13", "KGF 1"),
            ]
        else:
            images = [
                ("https://avatars.mds.yandex.net/i?id=df804c6ebcbe4a1fa1334d6aec638d7c9d4a5a25-10355098-images-thumbs&n=13", "KGF 2"),
                ("https://avatars.mds.yandex.net/i?id=03f419917a0d49f40c55b1898195b7fcb31a6736-9674922-images-thumbs&n=13", "KGF 2"),
                ("https://avatars.mds.yandex.net/i?id=b8bbf0bd1691c1c136c91bd53688e11dc00c2345-4477078-images-thumbs&n=13", "KGF 2"),
                ("https://avatars.mds.yandex.net/i?id=d736c13ff70014e2e4be8e0c7df821ca3162b08f-5339847-images-thumbs&n=13", "KGF 2"),
                ("https://avatars.mds.yandex.net/i?id=c6a8b60513d0fa65bcfed5f9cb3a0c1bdea7fb4e-6622507-images-thumbs&n=13", "KGF 2"),
                ("https://avatars.mds.yandex.net/i?id=544bee2d3e6f5b394863ff75163ce025afe88e8a-4955124-images-thumbs&n=13", "KGF 2"),
            ]
    elif key == "bahubali":
        ch = show_radio("bahubali_part")
        if ch == "Part 1":
            images = [
                ("https://avatars.mds.yandex.net/i?id=f032c479824a5c4fc0d851ca9ebdfe3cf5db119f-5239620-images-thumbs&n=13", "Bahubali 1"),
                ("https://avatars.mds.yandex.net/i?id=e5ea23e78567f4d86f213e3cca9527ee2c36bddd-4297485-images-thumbs&n=13", "Bahubali 1"),
                ("https://avatars.mds.yandex.net/i?id=1401ea67484a21f57e295981643847c01d67d2d8-4499646-images-thumbs&n=13", "Bahubali 1"),
                ("https://avatars.mds.yandex.net/i?id=7c42c9ebd201cd8158ff86c73ce70945373df7df-4713335-images-thumbs&n=13", "Bahubali 1"),
                ("https://navbharattimes.indiatimes.com/thumb/89112017/bahubali-before-the-beginning-89112017.jpg?imgsize=57484&width=1200&height=900&resizemode=75", "Bahubali 1"),
                ("https://avatars.mds.yandex.net/i?id=63d97fe13e33bb26a05d524ea57c69abf2582ea2-5147200-images-thumbs&n=13", "Bahubali 1"),
            ]
        else:
            images = [
                ("https://avatars.mds.yandex.net/i?id=110fed4f8ae780e9e46a795d8605080358c3d4a3-4719550-images-thumbs&n=13", "Bahubali 2"),
                ("https://avatars.mds.yandex.net/i?id=f333265bfcefad37bf067345f512049763967ebd-5279994-images-thumbs&n=13", "Bahubali 2"),
                ("https://avatars.mds.yandex.net/i?id=afb047fb9a68a4f5491a660eb5614fb99b035636-4120615-images-thumbs&n=13", "Bahubali 2"),
                ("https://avatars.mds.yandex.net/i?id=aac25a24639fc4a2954f035463208832c369a6a5-4055900-images-thumbs&n=13", "Bahubali 2"),
                ("https://avatars.mds.yandex.net/i?id=2db06ab39fbc3e50dea0ee7c982aa0e6892f2e74-12321751-images-thumbs&n=13", "Bahubali 2"),
                ("https://avatars.mds.yandex.net/i?id=4f3d56c779eaf8ae30183fe9400161822f877757-10236784-images-thumbs&n=13", "Bahubali 2"),
            ]
    elif key == "dhurandhar":
        ch = show_radio("dhurandhar_part")
        if ch == "Part 1":
            images = [
                ("https://avatars.mds.yandex.net/i?id=046aa2619737a916286797ca33b99ad7eb690e4d-13081656-images-thumbs&n=13", "Dhurandhar 1"),
                ("https://avatars.mds.yandex.net/i?id=7e3dac668c3ce5df2967770ecfa005eea7a2f74c-5694385-images-thumbs&n=13", "Dhurandhar 1"),
                ("https://avatars.mds.yandex.net/i?id=1046576ac130d4bf19bc75055322b37578dfc51f-5877978-images-thumbs&n=13", "Dhurandhar 1"),
                ("https://avatars.mds.yandex.net/i?id=a55249f3f7406c19b7f65f894d238b8852a1c271-5232856-images-thumbs&n=13", "Dhurandhar 1"),
                ("https://avatars.mds.yandex.net/i?id=f0ff83c8e7569873dc03f919d746d8f378ebb20c-5221061-images-thumbs&n=13", "Dhurandhar 1"),("https://avatars.mds.yandex.net/i?id=4968d15d2c7167a04b402a26aafdc40e0108a18c-5233671-images-thumbs&n=13", "Dhurandhar 1"),
                ("https://avatars.mds.yandex.net/i?id=42ee02bc4c0788ad6a93fded61db9391185d02a8-5390929-images-thumbs&n=13", "Dhurandhar 1"),
                ("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfVY2mjyBjTVcG7-ZGEtVmXGRWO4W3RI6PsA&s", "Dhurandhar 1"),
            ]
        else:
            images = [
                ("https://avatars.mds.yandex.net/i?id=2656039e6dd84383265d4b22fb0891181c76ae4e-5869499-images-thumbs&n=13", "Dhurandhar 2"), 
                ("https://avatars.mds.yandex.net/i?id=f78f403fc9817d6350ad0e6b41290da33ee75ce1-5603780-images-thumbs&n=13", "Dhurandhar 2"),
                ("https://avatars.mds.yandex.net/i?id=f533ca5182931218497b600ce09f8a5085e19ace-5165563-images-thumbs&n=13", "Dhurandhar 2"),
                ("https://avatars.mds.yandex.net/i?id=d363e07b1fe89e83b6604a67e01fc2b78e6c232c-5888889-images-thumbs&n=13", "Dhurandhar 2"),
                ("https://avatars.mds.yandex.net/i?id=abe30e908bbbd1546b954bc925ab78e4ddd4237a-5905003-images-thumbs&n=13", "Dhurandhar 2"),
                ("https://avatars.mds.yandex.net/i?id=be9fac5860af31480214002520e44ef56e7e2094-4568535-images-thumbs&n=13", "Dhurandhar 2"),
            ]



    elif key in images_data:
        images = images_data[key]

    else:
        st.info("No images available for this movie yet.")
        return
    
    if not images:
        st.warning("No images found.")
        return

    show_progress()

    cols = st.columns(2)
    for i, img in enumerate(images):
        with cols[i % 2]:
            st.image(img[0], caption=img[1])


def show_songs(movie):
    key = movie.lower()
    st.subheader("🎵 Songs")

    songs = {
      
        "chhaava": [
                "https://open.spotify.com/embed/track/6fkXfRbjbB7TnIoYK6LmZo",  
                "https://open.spotify.com/embed/track/20tZ0QylontantdwsEEwIr",  
                "https://open.spotify.com/embed/track/6qRHJNT6oILLhehqzxLAQh", 
                "https://open.spotify.com/embed/track/1By5OBVJcuvs5NncDZPwRM",  
                "https://open.spotify.com/embed/track/0R97OfArQkB9hOptu72NiV", 
                "https://open.spotify.com/embed/track/3UPu25TtH4LVHbH5RBhS4P", 
                "https://open.spotify.com/embed/track/3O1RVvHt3xdeo5VNSe7uts", 
        ],
        "saiyaara": [
            "https://open.spotify.com/embed/track/5SSZtFWdrmFV4MxtlRA13N",  
            "https://open.spotify.com/embed/track/3fDHLGL5SYrf65ysmOhyqc",  
            "https://open.spotify.com/embed/track/5nMv7iOp4NxJaWx0t8361M",  
            "https://open.spotify.com/embed/track/5XhurUCCVimKqszDzNXxoh", 
            "https://open.spotify.com/embed/track/5X6GMFZrIYmbhbhLY2Kv23", 
            "https://open.spotify.com/embed/track/1uRTH9LeFh40tFYlq48vcy",  
            "https://open.spotify.com/embed/track/2A7uwnEzSin7nf0498AE3x",  
        ],
        "rrr": [
            "https://open.spotify.com/embed/track/26cHFZNNF8wXOYJSH2Si4B",  
            "https://open.spotify.com/embed/track/6Riz3j8nRENg1e7ejJrjb4",  
            "https://open.spotify.com/embed/track/3aUfD75nYgejjhXNv0nfFO", 
            "https://open.spotify.com/embed/track/0mTek8vH6XIjcJSSGmz1kL",  
            "https://open.spotify.com/embed/track/7yETIAJYaUT2K56RPhI6JC", 
            "https://open.spotify.com/embed/track/4hxA06BamdTFK5r9toAupX",  
            "https://open.spotify.com/embed/track/31fXnOzbWufydBV2MTRfJi", 
        ],
        "pathaan": [
            "https://open.spotify.com/embed/track/49mPah10lutnHaU0NLf97t",  
            "https://open.spotify.com/embed/track/6FAYpZ4jve8vpvTwUvjK6H",  
            "https://open.spotify.com/embed/track/7l00c4RIiRh9MngY4Mt6jG",  
            "https://open.spotify.com/embed/track/067vgMqZQ7GdBeRc98bwev",  
        ],
        "mahavatar narsimha": [
            "https://open.spotify.com/embed/track/07IBhb2VlrOUCdi2FlR2tG", 
            "https://open.spotify.com/embed/track/3vkaaBS55rzI6ZKrfWyXkN",  
            "https://open.spotify.com/embed/track/35GPrqnJ64ofvWtE4CTMRY",  
            "https://open.spotify.com/embed/track/2mxfIlgOGXx2EPi50uXNNk",  
            "https://open.spotify.com/embed/track/7jOogU3dk8bR3mELD1dUp6",  
            "https://open.spotify.com/embed/track/35GL10IPiuoJofRO2MTxNx",  
            "https://open.spotify.com/embed/track/6OkKrtBY6tROnQO8bJqPVi", 
        ],
        "laalo": [
            "https://open.spotify.com/embed/track/2HYpjZhTbJo6g5xANbmaKS",  
            "https://open.spotify.com/embed/track/2NAAKFUdUAVjhJ47A9N3rC",  
            "https://open.spotify.com/embed/track/6Y3slmwRoFNY5Dh05YhZxw", 
            "https://open.spotify.com/embed/track/3YvoNsui4X5QCT1EbcRErX",  
            "https://open.spotify.com/embed/track/34pAXgGDTgJBHH0JqUiI3e",  
            "https://open.spotify.com/embed/track/4top9bnkKR7V0qzBQdusRn",  
            "https://open.spotify.com/embed/track/1562sW6y1DTaObngmoy8X4",  
        ],
     }

    if key == "pushpa":
        ch = show_radio("pushpa_song_part")
        if ch == "Part 1":
            song_list = [
                "https://open.spotify.com/embed/track/4aVsN0F48bL9KuD330V51P", 
                "https://open.spotify.com/embed/track/1xkkeOtWvzmhjgLqxMJ3zR", 
                "https://open.spotify.com/embed/track/3eYJSa9PPW5f8piMpf1tMr",  
                "https://open.spotify.com/embed/track/3hRnAaDYPEIGTMS6JI1dle",
                "https://open.spotify.com/embed/track/0jenJohxJTFQTuqi5Js0Dg",
            ]
        else:
            song_list = [
                        
            "https://open.spotify.com/embed/track/1o0bFBGkxgxCnu6mg2YrP1",  
            "https://open.spotify.com/embed/track/2ZDOzySC2g3YF1p26TPzBt",
            "https://open.spotify.com/embed/track/3E2alxlOoe5EURfec217Uu", 
            "https://open.spotify.com/embed/track/0Tvybk3jWj7usdP3LALmHI",  
            "https://open.spotify.com/embed/track/6FaojuQhUfwYSwFgdXZ5B3", 

            ]

    elif key == "kgf":
        ch = show_radio("kgf_song_part")
        if ch == "Part 1":
            song_list = [
            "https://open.spotify.com/embed/track/6kWYigBhkWT2EINUNNtYr4",  
            "https://open.spotify.com/embed/track/0mgaFholZbrMDc2OPBnVn6", 
            "https://open.spotify.com/embed/track/3wROHeaQRxusGFD4Pu1GTx", 
            "https://open.spotify.com/embed/track/2DYiisZs93UpoPqqALizFL",  
            "https://open.spotify.com/embed/track/5oak8iqn2yxLuSEO5W2oOp",  
            "https://open.spotify.com/embed/track/4aO9pvX2kTJTdmJqc0YRsr", 
        ]
        else:
            song_list = [    
            "https://open.spotify.com/embed/track/4RpWyOGMA0P4BE4MYBvVGT",  
            "https://open.spotify.com/embed/track/0qvMtmlk083p2tzGAYsotE", 
            "https://open.spotify.com/embed/track/2WAEq2jp8u5hA2oazj1ZOd", 
            "https://open.spotify.com/embed/track/3R0v8zXfoweBeSbWZzRBoW",  
        ]
    elif key == "bahubali":
        ch = show_radio("bahubali_song_part")
        if ch == "Part 1":
            song_list = [
            "https://open.spotify.com/embed/track/0swPjKhpOexUZtxTY6foXk",   
            "https://open.spotify.com/embed/track/31ZgC5ifKFLJoxzaOxukjv",  
            "https://open.spotify.com/embed/track/61oEpy6prYHrlOe0dGEJcE",
            "https://open.spotify.com/embed/track/3mWXDlDr1iZsaxgFz3vrrD",  
            "https://open.spotify.com/embed/track/4J6Hy70BKRg0YZoAKHA24W",  
            "https://open.spotify.com/embed/track/3sKfLcMJPAptbFLnCB1Ytr",  
            "https://open.spotify.com/embed/track/61Y3nM4caYiAhcY9ogq2gv",
        ]
        else:
            song_list = [ 
                "https://open.spotify.com/embed/track/2S3KDCaxzKx8fvHatpnANw",  
                "https://open.spotify.com/embed/track/6PS5jdC3iUx1pnMB6pyBnX",  
                "https://open.spotify.com/embed/track/5iVyx2WMd7lwkWeXIs6cid",  
                "https://open.spotify.com/embed/track/6Dzrw3MQFXeAGnJrfDUYun", 
                "https://open.spotify.com/embed/track/1khRXKcOsjsChxKf3zsgg3",
            ]
    elif key == "dhurandhar":
        ch = show_radio("dhurandhar_song_part")
        if ch == "Part 1":
            song_list = [    
            "https://open.spotify.com/embed/track/5xKr4HfdnYLMDmAJZkOuBc", 
            "https://open.spotify.com/embed/track/7DonHcAdu5FHzLNESEEOuj", 
            "https://open.spotify.com/embed/track/5MCbGWnNLLjoHpbDO3BOgi", 
            "https://open.spotify.com/embed/track/58Y6MtOFn040fJj367NYsr", 
            "https://open.spotify.com/embed/track/5NK3IhIeIXQmOKK5EiSRra", 
            "https://open.spotify.com/embed/track/0R7grQWU1dRxiOQGIqZm0Z", 
            "https://open.spotify.com/embed/track/6JIquezleHbiqFOSuvBlxw", 
            "https://open.spotify.com/embed/track/2dQMisG0lyz6Z8J4zYdAsG", 
            "https://open.spotify.com/embed/track/3SVgtZSEqPNga5pKOJLCDZ", 
            "https://open.spotify.com/embed/track/2nnDPEbNxnBKq5RG6sObTg", 
            "https://open.spotify.com/embed/track/3Zg5ENFvbucf41iPRvPcHn", 
        ]
            
        else:
            song_list = [
            "https://open.spotify.com/embed/track/157BtwkY54FQ3Xl8DsTso1",  
            "https://open.spotify.com/embed/track/5icrEfubHCXlHEue9YUT3q",  
            "https://open.spotify.com/embed/track/4aWTPC6cuebk9zSpW1PY1Y",  
            "https://open.spotify.com/embed/track/0KjTF8c2qGUJBCuAskhsGT",  
            "https://open.spotify.com/embed/track/335fJmufeLViovmc7MjCdb",  
            "https://open.spotify.com/embed/track/1I7yw0J5KpUaWhdBviGlON",  
            "https://open.spotify.com/embed/track/2NhPxmtxBFZQ8Nr583Iqqt",  
            "https://open.spotify.com/embed/track/17HVvCRmEq7ynQ6GG6CM3Q",  
            "https://open.spotify.com/embed/track/79WcL9b7spam7V0nBJNa6O",  
            "https://open.spotify.com/embed/track/12YztU3FVYQAio98iwGkVr",  
            "https://open.spotify.com/embed/track/6xwKNAUHeo2DbWNAPi8aEy",  
            "https://open.spotify.com/embed/track/363ZPkL810HJ3BIcDHRWb9",  
            "https://open.spotify.com/embed/track/09WTiAB81RmPHae2BPjtaQ",  
            "https://open.spotify.com/embed/track/4QAhkj55nfiPtYyqkooIzu",  
        ]
            
    else:
        song_list = songs.get(key, [])

    if song_list:
        for url in song_list:
            components.iframe(url, height=100)
    else:
        st.warning("Songs not available for this movie.")


def show_poster(movie):
    key = movie.lower()
    st.subheader("🎬 Movie Poster")

    posters = []
   

    if key == "pushpa":
        ch = show_radio("pushpa_poster_part")
        if ch == "Part 1":
            posters = [
                ("https://wallpapercave.com/wp/wp11468809.jpg", "Pushpa 1"),
                ("https://cdn.bollywoodmdb.com/movies/largethumb/2021/pushpa/pushpa-poster-4.jpg", "Pushpa 1"),
                ("https://www.tvguide.com/a/img/catalog/provider/2/2/2-46985dc2b9273771732350eda9e5ea47.jpg", "Pushpa 1"),
            ]
        else:
            posters = [
                ("https://image.tmdb.org/t/p/original/gpNcQfQ4YGtFwEcrjcK9HxVM2KF.jpg", "Pushpa 2"),
                ("https://images.fandango.com/ImageRenderer/820/0/redesign/static/img/default_poster.png/0/images/masterrepository/fandango/238502/pushpa2therule-posterart-sm.jpg", "Pushpa 2"),
                ("https://avatars.mds.yandex.net/i?id=c5e8d1513cee2593fec2fabf16511d53b195a3846f688ab4-12982376-images-thumbs&n=13", "Pushpa 2"),
            ]

    
    elif key == "kgf":
        ch = show_radio("kgf_poster_part")
        if ch == "Part 1":
            posters = [
                ("https://mir-s3-cdn-cf.behance.net/project_modules/disp/b0276774284099.5c2a29444d4a0.png", "KGF 1"),
                ("https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/869d6274284099.5c2a29444e565.png", "KGF 1"),
                ("https://wallpapercave.com/wp/wp4019385.jpg", "KGF 1"),
            ]
        else:
            posters = [
                ("https://avatars.mds.yandex.net/i?id=531dc95f430bfb711c949e65fe5135b97ab2455f-10267148-images-thumbs&n=13", "KGF 2"),
                ("https://wallpapercave.com/wp/wp11144087.jpg", "KGF 2"),
                ("https://avatars.mds.yandex.net/i?id=99d2f5dcef6c0f4ce149ecc4549bb72526463cf4-12731078-images-thumbs&n=13", "KGF 2"),
                
            ]
    elif key == "bahubali":
        ch = show_radio("bahubali_poster_part")
        if ch == "Part 1":
            posters = [
                ("https://i.pinimg.com/originals/3d/4b/f7/3d4bf791f4f797a4767772c8be8e04d7.jpg", "Bahubali 1"),
                ("https://wallpapercave.com/wp/wp1851909.jpg", "Bahubali 1"),
                ("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT7gupDIjEPfvmjENLhHqL0bBOwZCnmR7e_uA&s", "Bahubali 1"),
            ]
        else:
            posters = [
                ("https://wallpapercave.com/wp/wp6728411.jpg", "Bahubali 2"),
                ("https://i.pinimg.com/736x/40/aa/4e/40aa4e597b0fb5c7d00bb54b1b2a0362.jpg", "Bahubali 2"),
                ("https://cinemachaat.com/wp-content/uploads/2017/04/baahubali-2-poster.jpg", "Bahubali 2"),
               
            ]
    elif key == "dhurandhar":
        ch = show_radio("dhurandhar_poster_part")
        if ch == "Part 1":
            posters = [
                ("https://images.fandango.com/ImageRenderer/200/0/redesign/static/img/default_poster--dark-mode.png/0/images/masterrepository/Fandango/243483/Dhurandhar--Poster-Image.jpg", "Dhurandhar 1"),
                ("https://knowlepedia.org/images/4/4b/Dhurandhar_Poster.jpg", "Dhurandhar 1"),
                ("https://stat5.bollywoodhungama.in/wp-content/uploads/2025/06/Dhurandar.jpg", "Dhurandhar 1"),
                ("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT79BIRk7-wWElFjzNvaCkHC-au2TqzwnKgUw&s", "Dhurandhar 1"),
            ]
        else:
            posters = [
                ("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj7x0ANDbxiNZVKvv_GZoAxpAkHCZp5dQwb5WB92OjJd1-5MckfM4cIT0ZKgx6-BPoLNl9b81Oi5Sgu-_kgWVcG7S-ATMvLUZRX1N6vpFE1l2vQqamOKSHs_xEwuxbXTs_msL1MBw0sVKl-aQJcEYP7mTRZcgVkJP3ioAmAD45bTJ1eFfD8qpVwZxTul7g/s2000/dhu2.jpg","Dhurandhar 2"),
                ("https://image.tmdb.org/t/p/original/po7U3As6Jp2zG9RopavoZMkdnr1.jpg","Dhurandhar 2"),
                ("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSjPJHUON3k8tYQjP1cQLtsWFDz7smrTUDWKQ&s","Dhurandhar 2"),
            ]

    else:
        poster_data = {
                "chhaava": [
                    ("https://m.media-amazon.com/images/M/MV5BMWI4N2Y5NWUtNzEwOC00YjYzLWEzY2ItN2YwYTIxYzBjZGZmXkEyXkFqcGc@._V1_.jpg","Chhaava"),
                    ("https://filmifiles.com/wp-content/uploads/2025/01/WhatsApp-Image-2025-01-24-at-6.31.36-PM.jpeg","Chhaava"),
                    ("https://stat4.bollywoodhungama.in/wp-content/uploads/2023/10/Chhaava.jpg","Chhaava"),
                ],

                "saiyaara": [
                    ("https://stat5.bollywoodhungama.in/wp-content/uploads/2025/05/Saiyaara-2-1.jpg","Saiyaara"),
                    ("https://media-cache.cinematerial.com/p/500x/7bx0lsht/saiyaara-indian-movie-poster.jpg?v=1757577090","Saiyaara"),
                    ("https://i.ytimg.com/vi/9r-tT5IN0vg/maxresdefault.jpg","Saiyaara"),
                    
                ],

                "rrr": [
                    ("https://wallpapercave.com/wp/wp13464642.jpg","RRR"),
                    ("https://image.tmdb.org/t/p/original/nEufeZlyAOLqO2brrs0yeF1lgXO.jpg","RRR"),
                    ("https://mir-s3-cdn-cf.behance.net/project_modules/max_3840/c7d5e4140074961.623b147c53ca8.jpg","RRR"),
                ],
                "pathaan": [
                    ("https://wallpaperaccess.com/full/8642989.jpg","Pathaan"),
                    ("https://wallpaperaccess.com/full/8641599.jpg","Pathaan"),
                    ("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjMJ-KMGv6Fk3oYym3i5zayTxWxidw17bpqT6E_SHm0AaDowpLliEpTMGrOsxegaFAIMgsNUXFeuTtWJV2qYRi0L8JjkPZ8vGqjl8p_dOQMJPiHKEbVmE6sYj92UOYmHnUGRBrUTsBpAAMsI1yi49u6AMCW64Jlwi4GuOEnPIJmP460BIdjgk46reN5/s1482/Pathaan-Movie-Poster.jpg","Pathaan"),
                ],
                "mahavatar narsimha": [
                    ("https://media-cache.cinematerial.com/p/500x/zdo6fxlx/mahavatar-narsimha-indian-movie-poster.jpg?v=1753906903","Mahavatar Narsimha"),
                    ("https://images.filmibeat.com/ph-big/2025/07/mahavatar-narsimha1753102502_0.jpg","Mahavatar Narsimha"),
                    ("https://images.filmibeat.com/ph-big/2025/07/mahavatar-narsimha1752149128_2.jpeg","Mahavatar Narsimha"),

                ],
                "laalo": [
                    ("https://i.ytimg.com/vi/dG3a81ZE-x8/maxresdefault.jpg","Laalo"),
                    ("https://avatars.mds.yandex.net/i?id=a1bc6a70cca2aba4ed3aed1cb724131882dba357-5447357-images-thumbs&n=13","Laalo"),
                    ("https://avatars.mds.yandex.net/i?id=fa5eeb7c6d684c51da0dfdbc5db904faaccc2e9c-5174345-images-thumbs&n=13","Laalo"),
                ],
        }
        posters = poster_data.get(key, [])

    if not posters:
        st.warning("Poster not available for this movie.")
        return

  
    cols = st.columns(2)
    for i, poster in enumerate(posters):
        with cols[i % 2]:
            st.image(poster[0], caption=poster[1], use_container_width=True)

import streamlit as st

def show_ratings(movie):
    
    ratings = {
        "chhaava": {
            "IMDb": "7.3/10",
            "Rotten Tomatoes": "85%",
            "Metacritic": "72/100"
        },
        "saiyaara": {
            "IMDb": "7.5/10",
            "Rotten Tomatoes": "65%",
            "Metacritic": "72/100",
        },
        "rrr": {
            "IMDb": "7.8/10",
            "Rotten Tomatoes": "95%",
            "Metacritic": "83/100"
        },
        "pushpa": {
            "IMDb": "7.4/10",
            "Rotten Tomatoes": "76%",
            "Metacritic": "67/100"
        },
        "kgf": {
            "IMDb": "8.2/10",
            "Rotten Tomatoes": "76%",
            "Metacritic": "67/100"

        },
        "pathaan": {
            "IMDb": "7.4/10",
            "Rotten Tomatoes": "76%",
            "Metacritic": "67/100"
        },
        "mahavatar narsimha": {
                "IMDb": "N/A",
                "Rotten Tomatoes": "N/A",
                "Metacritic": "N/A"
        },
        "bahubali": {
                "IMDb": "8.2/10",
                "Rotten Tomatoes": "86%",
                "Metacritic": "N/A"
        },
        "laalo": {
            "IMDb": "6.8/10 (approx)",
            "Rotten Tomatoes": "45% (approx)",
            "Metacritic": "57/100 (approx)"
        },
        "dhurandhar": {
            "IMDb": "N/A",
            "Rotten Tomatoes": "N/A",
            "Metacritic": "N/A"
        }
    }
    key = movie.lower()
    
    if key in ratings:
        st.subheader("🌟 Ratings")
        for platform, value in ratings[key].items():
            st.write(f"**{platform}**: {value}")
    else:
        st.warning("Ratings not available for this movie.")

def show_trailer(movie):

    key = movie.lower()
    st.subheader("🎬 Movie Trailer")

    trailers = {
        "chhaava": [
            "https://youtu.be/77vRyWNqZjM",
            "https://youtu.be/nsC5PhXS19Y"
        ],
        "saiyaara": ["https://youtu.be/9r-tT5IN0vg"],
        "rrr": ["https://youtu.be/GY4BgdUSpbE"],
        "pathaan": ["https://youtu.be/vqu4z34wENw"],
        "mahavatar narsimha": ["https://youtu.be/p7eE_dn9u4k"],
        "laalo": ["https://youtu.be/TVUPpmkrvVw"],
    }

    if key == "pushpa":
        ch = show_radio("pushpa_trailer_part")
        if ch == "Part 1":
            trailer_list = ["https://youtu.be/ou6h-22tMnA"]
        else:
            trailer_list = ["https://youtu.be/1kVK0MZlbI4"]

    elif key == "kgf":
        ch = show_radio("kgf_trailer_part")
        if ch == "Part 1":
            trailer_list = ["https://youtu.be/-KfsY-qwBS0?si=oGS3k_tGS4-5YYF4"]
        else:
            trailer_list = ["https://youtu.be/_7b1647tH74?si=L-z-xbxrYyQA0BP8"]

    elif key =="bahubali":
        ch = show_radio("bhubali_trailer_part")
        if ch == "Part 1":
            trailer_list = ["https://youtu.be/VdafjyFK3ko?si=_1pkBeGBYWE1oHzU"]
        else:
            trailer_list = ["https://youtu.be/G62HrubdD6o?si=wf4HVwrLG2MTBTrf"]

    elif key =="dhurandhar":
        ch = show_radio("dhurandhar_trailer_part")
        if ch == "Part 1":
            trailer_list = ["https://youtu.be/BKOVzHcjEIo?si=gtGCLEgBQ34zkkVo"]
        else:
            trailer_list = ["https://youtu.be/NHk7scrb_9I?si=iKFrrmdAHyW80J-Z"]

    else:
        trailer_list = trailers.get(key)

    if trailer_list:
        for url in trailer_list:
            st.video(url)
    else:
        st.warning("Trailer not available for this movie.")

def show_about(movie):
    key = movie.lower()
    st.subheader("About " + movie)

    movie_data = {
        # ─────────────────────────────────────────────
        "chhaava": {
            "year": "2025",
            "genre": "Action, Historical Drama",
            "director": "Laxman Utekar",
            "wikipedia": {
                "single": "https://en.wikipedia.org/wiki/Chhaava_(film)"
            },
            "cast": [
                {
                    "name": "Vicky Kaushal",
                    "role": "Chhatrapati Sambhaji Maharaj",
                    "wikipedia": "https://en.wikipedia.org/wiki/Vicky_Kaushal",
                    "images": ["https://assets.telegraphindia.com/telegraph/2024/Jul/1720682532_vicky-kaushal.jpg"],
                },
                {
                    "name": "Rashmika Mandanna",
                    "role": "Yesubai Bhonsale",
                    "wikipedia": "https://en.wikipedia.org/wiki/Rashmika_Mandanna",
                    "images": ["https://th.bing.com/th/id/OIP.Otmyb33p_3_AU1TjKyFoHQHaFj?w=184&h=138&c=7&r=0&o=7&pid=1.7&rm=3"],
                },
                {
                    "name": "Akshaye Khanna",
                    "role": "Aurangzeb",
                    "wikipedia": "https://en.wikipedia.org/wiki/Akshaye_Khanna",
                    "images": ["https://www.bing.com/th/id/OIP.JBe4-KIkKFfdGDi_tERr6wHaKD?w=180&h=245&c=8&rs=1&qlt=90&o=6&pid=3.1&rm=2"],
                },
                {
                    "name": "Ashutosh Rana",
                    "role": "Hambir Rao",
                    "wikipedia": "https://en.wikipedia.org/wiki/Ashutosh_Rana",
                    "images": ["https://th.bing.com/th/id/OIP.txT6pNnW4_xhNXxAwpcQ2wHaJ4?w=135&h=180&c=7&r=0&o=7&pid=1.7&rm=3"],
                },
                {
                    "name": "Divya Dutta",
                    "role": "Soyrabai",
                    "wikipedia": "https://en.wikipedia.org/wiki/Divya_Dutta",
                    "images": ["https://th.bing.com/th/id/OIP.AS53s1Ya2lP9wqahwZh1XwHaE8?w=184&h=123&c=7&r=0&o=7&pid=1.7&rm=3"],
                },
                {
                    "name": "Vineet Kumar Singh",
                    "role": "Kavi Kalash",
                    "wikipedia": "https://en.wikipedia.org/wiki/Vineet_Kumar_Singh",
                    "images": ["https://th.bing.com/th/id/OIP.irINPPEHMPWYQZVgPbd_XgHaEK?w=299&h=180&c=7&r=0&o=7&pid=1.7&rm=3"],
                },
                {
                    "name": "Diana Penty",
                    "role": "Zeenat",
                    "wikipedia": "https://en.wikipedia.org/wiki/Diana_Penty",
                    "images": ["https://th.bing.com/th/id/OIP.orXHgP8cMUBvDdJiJqMOngHaJQ?w=184&h=230&c=7&r=0&o=7&pid=1.7&rm=3"],
                },
                {
                    "name": "Neil Bhoopalam",
                    "role": "Akbar",
                    "wikipedia": "https://en.wikipedia.org/wiki/Neil_Bhoopalam",
                    "images": ["https://th.bing.com/th/id/OIP.fW01iXI2OYCWJZ-c8IGuLgHaEK?w=279&h=180&c=7&r=0&o=7&pid=1.7&rm=3"],
                },
                {
                    "name": "Danish Pandor",
                    "role": "Supporting Role",
                    "wikipedia": "https://en.wikipedia.org/wiki/Danish_Pandor",
                    "images": ["https://th.bing.com/th/id/OIP.FkkgPp2vVJ-OCgwkmUyy_wHaGc?w=192&h=180&c=7&r=0&o=7&pid=1.7&rm=3"],
                },
            ],
        },

        # ─────────────────────────────────────────────
        "saiyaara": {
            "year": "2025",
            "genre": "Romantic Drama",
            "director": "Mohit Suri",
            "wikipedia": {
                "single": "https://en.wikipedia.org/wiki/Saiyaara_(film)"
            },
            "cast": [
                {
                    "name": "Ahaan Panday",
                    "role": "Veer",
                    "wikipedia": "https://en.wikipedia.org/wiki/Ahaan_Panday",
                    "images": ["https://th.bing.com/th/id/OIP.LYKXs7kR2fjIyZywO7K44AAAAA?w=200&h=200&c=10&o=6&pid=genserp&rm=2"],
                },
                {
                    "name": "Aneet Padda",
                    "role": "Saiyaara",
                    "wikipedia": "https://en.wikipedia.org/wiki/Aneet_Padda",
                    "images": ["https://assets.telegraphindia.com/telegraph/2025/Aug/1756115195_aneet-padda-lead.jpg"],
                },
                {
                    "name": "Mohit Suri",
                    "role": "Director",
                    "wikipedia": "https://en.wikipedia.org/wiki/Mohit_Suri",
                    "images": ["https://www.bollywoodbiography.in/wp-content/uploads/2022/01/mohit-suri.jpg"],
                },
            ],
        },

        # ─────────────────────────────────────────────
        "rrr": {
            "year": "2022",
            "genre": "Action, Drama",
            "director": "S. S. Rajamouli",
            "wikipedia": {
                "single": "https://en.wikipedia.org/wiki/RRR_(film)"
            },
            "cast": [
                {
                    "name": "N. T. Rama Rao Jr.",
                    "role": "Komaram Bheem",
                    "wikipedia": "https://en.wikipedia.org/wiki/N._T._Rama_Rao_Jr.",
                    "images": ["https://th.bing.com/th/id/OIP.dAG0gzywyck7tnXwcJuOGwHaE7?w=184&h=122&c=7&r=0&o=7&pid=1.7&rm=3"],
                },               
                {
                    "name": "Ram Charan",
                    "role": "Alluri Sitarama Raju",
                    "wikipedia": "https://en.wikipedia.org/wiki/Ram_Charan",
                    "images": ["https://wallpapers.com/images/hd/ram-charan-hd-sleek-portrait-5saotulfo921krrg.jpg"],
                },
                {
                    "name": "Alia Bhatt",
                    "role": "Sita",
                    "wikipedia": "https://en.wikipedia.org/wiki/Alia_Bhatt",
                    "images": ["https://th.bing.com/th/id/OIP.e2Q-IejE2QGFn4RhkwpDVAHaE8?w=274&h=183&c=7&r=0&o=7&pid=1.7&rm=3"],
                },
                {
                    "name": "Ajay Devgn",
                    "role": "Venkata Rama Raju (cameo)",
                    "wikipedia": "https://en.wikipedia.org/wiki/Ajay_Devgn",
                    "images": ["https://tse1.mm.bing.net/th/id/OIP.vLk66rHNiUOHArERP7uv8gHaEK?rs=1&pid=ImgDetMain&o=7&rm=3"],
                },
                {
                    "name": "Shriya Saran",
                    "role": "Sarojini",
                    "wikipedia": "https://en.wikipedia.org/wiki/Shriya_Saran",
                    "images": ["https://th.bing.com/th/id/OIP.lFt0W699hoYly4wga9CFzQHaJQ?w=184&h=230&c=7&r=0&o=7&pid=1.7&rm=3"],
                },
                {
                    "name": "Ray Stevenson",
                    "role": "Scott Buxton",
                    "wikipedia": "https://en.wikipedia.org/wiki/Ray_Stevenson",
                    "images": ["https://e3.365dm.com/23/05/1600x900/skynews-ray-stevenson-three-musketeers_6164223.jpg?20230522205658"],
                },
            ],
        },

        # ─────────────────────────────────────────────
        "pushpa": {
            "year": "2021 / 2024",
            "genre": "Action, Drama",
            "director": "Sukumar",
            "wikipedia": {
                "part1": "https://en.wikipedia.org/wiki/Pushpa:_The_Rise",
                "part2": "https://en.wikipedia.org/wiki/Pushpa:_The_Rule_%E2%80%93_Part_2"
            },
            "cast": [
                {
                    "name": "Allu Arjun",
                    "role": "Pushpa Raj",
                    "wikipedia": "https://en.wikiphedia.org/wiki/Allu_Arjun",
                    "images": ["https://th.bing.com/th/id/OIP.xoq6fJIwy1CZ7uHy_uZEnwHaFj?w=184&h=138&c=7&r=0&o=7&pid=1.7&rm=3"],
                },
                {
                    "name": "Rashmika Mandanna",
                    "role": "Srivalli",
                    "wikipedia": "https://en.wikipedia.org/wiki/Rashmika_Mandanna",
                    "images": ["https://th.bing.com/th/id/OIP.Otmyb33p_3_AU1TjKyFoHQHaFj?w=184&h=138&c=7&r=0&o=7&pid=1.7&rm=3"],
                },
                {
                    "name": "Fahadh Faasil",
                    "role": "Bhanwar Singh Shekhawat",
                    "wikipedia": "https://en.wikipedia.org/wiki/Fahadh_Faasil",
                    "images": ["https://assets.gqindia.com/photos/66d80264f0d3a00aed022985/16:9/w_1280,c_limit/Fahadh%20Faasil.jpg?mbid=social_retweet"],
                },
                {
                    "name": "Sunil",
                    "role": "Mangalam Srinu",
                    "wikipedia": "https://en.wikipedia.org/wiki/Sunil_(actor)",
                    "images": ["https://upload.wikimedia.org/wikipedia/commons/5/50/Sunil_Telugu_Film_Actor.jpg"],
                },
                {
                    "name": "Anasuya Bharadwaj",
                    "role": "Dakshayani",
                    "wikipedia": "https://en.wikipedia.org/wiki/Anasuya_Bharadwaj",
                    "images": ["https://content.tupaki.com/h-upload/2024/12/09/618059-gngknp0k.webp"],
                },
            ],
        },

        # ─────────────────────────────────────────────
        "kgf": {
            "year": "2018 / 2022",
            "genre": "Action, Drama",
            "director": "Prashanth Neel",
            "wikipedia": {
                "part1": "https://en.wikipedia.org/wiki/K.G.F:_Chapter_1",
                "part2": "https://en.wikipedia.org/wiki/K.G.F:_Chapter_2"
            },
            "cast": [
                {
                    "name": "Yash",
                    "role": "Rocky / Raja Krishnappa Bairya",
                    "wikipedia": "https://en.wikipedia.org/wiki/Yash_(actor)",
                    "images": ["https://th.bing.com/th/id/OIP.9SOPjkRn-SoDJ0wyYtyTywHaHa?w=178&h=180&c=7&r=0&o=7&pid=1.7&rm=3"],
                },
                {
                    "name": "Srinidhi Shetty",
                    "role": "Reena",
                    "wikipedia": "https://en.wikipedia.org/wiki/Srinidhi_Shetty",
                    "images": ["https://th.bing.com/th/id/OIP.4DZLr5F5ZmicGvHTJ4tbfwHaJQ?w=184&h=230&c=7&r=0&o=7&pid=1.7&rm=3"],
                },
                {
                    "name": "Raveena Tandon",
                    "role": "Ramika Sen (Chapter 2)",
                    "wikipedia": "https://en.wikipedia.org/wiki/Raveena_Tandon",
                    "images": ["https://th.bing.com/th/id/OIP.etzC2gS-SznkKEr0UUFntgHaEK?w=326&h=183&c=7&r=0&o=7&pid=1.7&rm=3"],
                },
                {
                    "name": "Sanjay Dutt",
                    "role": "Adheera (Chapter 2)",
                    "wikipedia": "https://en.wikipedia.org/wiki/Sanjay_Dutt",
                    "images": ["https://th.bing.com/th/id/OIP._C7tS47qf145w8a232QfkgHaE8?w=232&h=180&c=7&r=0&o=7&pid=1.7&rm=3"],
                },
                {
                    "name": "Prakash Raj",
                    "role": "Vijayendra Ingalagi",
                    "wikipedia": "https://en.wikipedia.org/wiki/Prakash_Raj",
                    "images": ["https://tse2.mm.bing.net/th/id/OIP._ijI-X1q7TaGtMb7flxhxgHaJ4?pid=ImgDet&w=474&h=632&rs=1&o=7&rm=3"],
                },
                {
                    "name":"Ramachandra Raju",
                    "role":"villainous (Chapter 1)",
                    "wikipedia":"https://en.wikipedia.org/wiki/Ramachandra_Raju",
                    "images":["https://th.bing.com/th/id/OIP.X9Rkc5bGDzdoLVVi2D9ABwHaJ9?w=125&h=180&c=7&r=0&o=7&pid=1.7&rm=3"]
                },             
            ],
        },

        # ─────────────────────────────────────────────
        "pathaan": {
            "year": "2023",
            "genre": "Action, Thriller",
            "director": "Siddharth Anand",
            "wikipedia": {
                "single": "https://en.wikipedia.org/wiki/Pathaan_(film)"
            },
            "cast": [
                {
                    "name": "Shah Rukh Khan",
                    "role": "Pathaan",
                    "wikipedia": "https://en.wikipedia.org/wiki/Shah_Rukh_Khan",
                    "images": ["https://ntvb.tmsimg.com/assets/assets/170054_v9_bc.jpg"],
                },
                {
                    "name": "Deepika Padukone",
                    "role": "Rubai",
                    "wikipedia": "https://en.wikipedia.org/wiki/Deepika_Padukone",
                    "images": ["https://tse1.explicit.bing.net/th/id/OIP.Ih9uK7z_wavQSrS8GVuhKQHaF7?w=1280&h=1024&rs=1&pid=ImgDetMain&o=7&rm=3"],
                },
                {
                    "name": "John Abraham",
                    "role": "Jim",
                    "wikipedia": "https://en.wikipedia.org/wiki/John_Abraham_(actor)",
                    "images": ["https://flxt.tmsimg.com/assets/294140_v9_bb.jpg"],
                },
                {
                    "name": "Dimple Kapadia",
                    "role": "Nandini",
                    "wikipedia": "https://en.wikipedia.org/wiki/Dimple_Kapadia",
                    "images": ["https://filmfare.wwmindia.com/content/2020/dec/dimple-kapadia-21608179784.jpg"],
                },
                {
                    "name": "Salman Khan",
                    "role": "Tiger (cameo)",
                    "wikipedia": "https://en.wikipedia.org/wiki/Salman_Khan",
                    "images": ["https://c.ndtvimg.com/2024-08/82s5epbo_salman-khan_625x300_27_August_24.jpg?im=FaceCrop,algorithm=dnn,width=540,height=720"],
                },
            ],
        },

        # ─────────────────────────────────────────────
        "mahavatar narsimha": {
            "year": "2025",
            "genre": "Mythological, Action",
            "director": "Aditya Sarpotdar",
            "wikipedia": {
                "single": "https://en.wikipedia.org/wiki/Mahavatar_Narsimha"
            },
           
        },

        # ─────────────────────────────────────────────
        "bahubali": {
            "year": "2015 / 2017",
            "genre": "Action, Drama, Fantasy",
            "director": "S. S. Rajamouli",
            "wikipedia": {
                "part1": "https://en.wikipedia.org/wiki/Baahubali:_The_Beginning",
                "part2": "https://en.wikipedia.org/wiki/Baahubali:_The_Conclusion"
            },
            "cast": [
                {
                    "name": "Prabhas",
                    "role": "Mahendra Baahubali / Amarendra Baahubali",
                    "wikipedia": "https://en.wikipedia.org/wiki/Prabhas",
                    "images": ["https://i.pinimg.com/originals/a9/49/30/a949303df9fca80e03c0affe7bbad12a.jpg"],
                },
                {
                    "name": "Rana Daggubati",
                    "role": "Bhallaladeva",
                    "wikipedia": "https://en.wikipedia.org/wiki/Rana_Daggubati",
                    "images": ["https://cdn.i-scmp.com/sites/default/files/styles/768x768/public/d8/images/canvas/2022/04/08/61c59de1-471a-4aad-814a-e9ebdff7ea41_feb78f30.jpg?itok=j0WOqR1P&v=1649405182"],
                },
                {
                    "name": "Anushka Shetty",
                    "role": "Devasena",
                    "wikipedia": "https://en.wikipedia.org/wiki/Anushka_Shetty",
                    "images": ["https://tse1.mm.bing.net/th/id/OIP.58aA2uDdeJOCtAhI4QqftgHaJe?rs=1&pid=ImgDetMain&o=7&rm=3"],
                },
                {
                    "name": "Tamannaah",
                    "role": "Avanthika",
                    "wikipedia": "https://en.wikipedia.org/wiki/Tamannaah",
                    "images": ["https://www.bollywoodhungama.com/wp-content/uploads/2025/02/Tamannaah-Bhatia-6-16.jpg"],
                },
                {
                    "name": "Sathyaraj",
                    "role": "Kattappa",
                    "wikipedia": "https://en.wikipedia.org/wiki/Sathyaraj",
                    "images": ["https://th.bing.com/th/id/OIP.xjRS39FJln_59YiFgjLwNwHaLH?w=184&h=276&c=7&r=0&o=7&pid=1.7&rm=3"],
                },
                {
                    "name": "Ramya Krishnan",
                    "role": "Sivagami",
                    "wikipedia": "https://en.wikipedia.org/wiki/Ramya_Krishnan",
                    "images": ["https://tse4.mm.bing.net/th/id/OIP.dgP5DKut93jrh5CRE--gXwHaI8?rs=1&pid=ImgDetMain&o=7&rm=3"],
                },
            ],
        },
        "laalo": {
            "year": "2025",
            "genre": "Devotional Drama",
            "director": "Ankit Sakhiya",
            "wikipedia": {
                "single": "https://en.wikipedia.org/wiki/Laalo_%E2%80%93_Krishna_Sada_Sahaayate"
            },
            "cast": [
                {
                    "name": "Karan Joshi",
                    "role": "Laalo",
                    "wikipedia": "https://en.wikipedia.org/wiki/Laalo_%E2%80%93_Krishna_Sada_Sahaayate",
                    "images": ["https://www.thekaranjoshi.com/images/gallery-5.jpg"],
                },
                {
                    "name": "Shruhad Goswami",
                    "role": "Lord Krishna",
                    "wikipedia": "https://en.wikipedia.org/wiki/Laalo_%E2%80%93_Krishna_Sada_Sahaayate",
                    "images": ["https://images.news18.com/ibnlive/uploads/2025/12/punit-canva-2025-12-16T105428.825-2025-12-33bb2bbfbb50fbd6550647f7ab262110-16x9.png"],
                },
                {
                    "name": "Reeva Rachh",
                    "role": "Leading Lady",
                    "wikipedia":"https://en.wikipedia.org/wiki/Laalo_%E2%80%93_Krishna_Sada_Sahaayate",
                    "images": ["https://th.bing.com/th/id/OIP.YhPhz_DSUtLVeR7LRw9z2QHaHV?w=182&h=180&c=7&r=0&o=7&pid=1.7&rm=3g"],
                },
            
            ],
        },

        # ─────────────────────────────────────────────
       "dhurandhar": {
        "year": "2025",
        "genre": "Action, Spy Thriller",
        "director": "Aditya Dhar",
        "wikipedia": {
            "part1": "https://en.wikipedia.org/wiki/Dhurandhar",
            "part2": "https://en.wikipedia.org/wiki/Dhurandhar:_The_Revenge"
        },
        "cast": [
            {
                "name": "Ranveer Singh",
                "role": "Hamza Ali Mazari / Jaskirat Singh (Lead - RAW Agent)",
                "wikipedia": "https://en.wikipedia.org/wiki/Ranveer_Singh",
                "images": [
                    "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Ranveer_Singh_in_2023_%281%29_%28cropped%29.jpg/250px-Ranveer_Singh_in_2023_%281%29_%28cropped%29.jpg"
                ],
            },
            {
                "name": "Akshaye Khanna",
                "role": "Rehman Dakait (Main Antagonist - Baloch Gang Leader)",
                "wikipedia": "https://en.wikipedia.org/wiki/Akshaye_Khanna",
                "images": [ "https://www.bing.com/th/id/OIP.JBe4-KIkKFfdGDi_tERr6wHaKD?w=180&h=245&c=8&rs=1&qlt=90&o=6&pid=3.1&rm=2"],
            },
            {
                "name": "Sanjay Dutt",
                "role": "SP Chaudhary Aslam (Lyari Task Force, Sindh Police)",
                "wikipedia": "https://en.wikipedia.org/wiki/Sanjay_Dutt",
                "images": ["https://th.bing.com/th/id/OIP._C7tS47qf145w8a232QfkgHaE8?w=232&h=180&c=7&r=0&o=7&pid=1.7&rm=3"],
            },
            {
                "name": "Arjun Rampal",
                "role": "Major Iqbal (ISI Officer)",
                "wikipedia": "https://en.wikipedia.org/wiki/Arjun_Rampal",
                "images": ["https://media.assettype.com/gulfnews/import/2019/03/07/tab_-Arjun-Rampal-1551950763025_16a30b2fea4_medium.jpg?w=1200&ar=40:21&auto=format,compress&ogImage=true&mode=crop&enlarge=true&overlay=false&overlay_position=bottom&overlay_width=100"],
            },
            {
                "name": "R. Madhavan",
                "role": "Ajay Sanyal (Director of IB - based on Ajit Doval)",
                "wikipedia": "https://en.wikipedia.org/wiki/R._Madhavan",
                "images": ["https://images.indianexpress.com/2025/01/R-Madhavan-1.jpg"],
            },
            {
        
                "name": "Sara Arjun",
                "role": "Yalina Jamali (Supporting)",
                "wikipedia": "https://en.wikipedia.org/wiki/Sara_Arjun",
                "images": ["https://starsbiohub.in/wp-content/uploads/2025/11/Screenshot-2025-11-21-230934.png"],
            },
            {
                "name": "Rakesh Bedi",
                "role": "Jameel Jamali (Senior Pakistani Politician)",
                "wikipedia": "https://en.wikipedia.org/wiki/Rakesh_Bedi",
                "images": ["https://alchetron.com/cdn/rakesh-bedi-6b123307-c1ac-4123-8de9-3562213262d-resize-750.jpeg"],
            },
            {
                "name": "Gaurav Gera",
                "role": "Mohammed Aalam (Juice Shop Owner - Hamza's Handler)",
                "wikipedia": "https://en.wikipedia.org/wiki/Gaurav_Gera",
                "images": ["https://th.bing.com/th/id/OIP.eD00jE9aV1BikXMARqDdHwHaFj?w=225&h=180&c=7&r=0&o=7&pid=1.7&rm=3"],
            },
            {
                "name": "Danish Pandor",
                "role": "Uzair Baloch (Rehman's Cousin & 2nd in Command)",
                "wikipedia": "https://en.wikipedia.org/wiki/Danish_Pandor",
                "images": ["https://th.bing.com/th/id/OIP.FkkgPp2vVJ-OCgwkmUyy_wHaGc?w=192&h=180&c=7&r=0&o=7&pid=1.7&rm=3"],
            },
        ],
    }
}

    if key not in movie_data:
        st.write("Details not available")
        return

    data = movie_data[key]

    # ── Movie info ──
    st.write("**Year:**", data["year"])
    st.write("**Genre:**", data["genre"])
    st.write("**Director:**", data["director"])

    # ── Wikipedia links ──
    wiki = data.get("wikipedia", {})
    if "single" in wiki:
        st.markdown(f"[🔗 Movie Wikipedia]({wiki['single']})")
    elif "part1" in wiki and "part2" in wiki:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"[🔗 Part 1 Wikipedia]({wiki['part1']})")
        with col2:
            st.markdown(f"[🔗 Part 2 Wikipedia]({wiki['part2']})")

    st.write("")

    # ── Cast section ──
    cast = data.get("cast", [])
    if cast:
        st.subheader(" Cast")
        for actor in cast:
            cols = st.columns([1, 2])
            with cols[0]:
                st.image(actor["images"][0], use_container_width=True)
            with cols[1]:
                st.write("**Name:**", actor["name"])
                st.write("**Role:**", actor["role"])
                st.markdown(f"[🔗 Wikipedia Profile]({actor['wikipedia']})")
            st.write("")
    else:
        st.info("Cast details coming soon.")




if "show_details" not in st.session_state:
    st.session_state.show_details = False

selected_movie = st.selectbox("Select Movie:", movie_list)

if st.button("Show Details"):
    st.session_state.show_details = True

if st.session_state.show_details:
    st.success(f"Selected Movie: {selected_movie}")

    tabs = st.tabs(["Image", "Song", "Rating", "Poster", "Trailer", "About"])

    with tabs[0]:
        show_gallery(selected_movie)

    with tabs[1]:
        show_songs(selected_movie)

    with tabs[2]:
        show_ratings(selected_movie)

        st.subheader(" Write a Review")
        review = st.text_area("Your Review")
        if st.button("Submit Review"):
            if review:
                st.write(" Your Review:", review)
            else:
                st.warning("Please write something!")

    with tabs[3]:
        show_poster(selected_movie)

    with tabs[4]:
        show_trailer(selected_movie)

    with tabs[5]:
        show_about(selected_movie)