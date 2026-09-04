"""
Seed script to populate cafes.db with initial cafe entries.
Run once: python seed_data.py
"""

from main import app, db, Cafe

with app.app_context():

    # ==================== KAUNAS CAFES ====================
    kaunas_cafes = [
        Cafe(name="Caffeine", map_url="https://maps.app.goo.gl/dzSgRVjdajadnipGA",
             img_url="https://atlondonbridge.com/wp-content/uploads/2019/02/Pano_9758_9761-Edit-190918_LTS_Science_Gallery-Medium-Crop-V2.jpg",
             location="Laisvės al.", has_sockets=True, has_toilet=True, has_wifi=False,
             can_take_calls=True, seats="50+", coffee_price="€3.00"),

        Cafe(name="Vero Cafe", map_url="https://maps.app.goo.gl/ZDWeVgGjomNRYrK78",
             img_url="https://images.squarespace-cdn.com/content/v1/5734f3ff4d088e2c5b08fe13/1555848382269-9F13FE1WQDNUUDQOAOXF/ke17ZwdGBToddI8pDm48kAeyi0pcxjZfLZiASAF9yCBZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpzV8NE8s7067ZLWyi1jRvJklJnlBFEUyq1al9AqaQ7pI4DcRJq_Lf3JCtFMXgpPQyk/copeland-park-bar-peckham",
             location="Laisvės al.", has_sockets=True, has_toilet=True, has_wifi=True,
             can_take_calls=False, seats="20-30", coffee_price="€3.00"),

        Cafe(name="Kavalierius", map_url="https://maps.app.goo.gl/BhN8k1kPCtkD8uCz6",
             img_url="https://lh3.googleusercontent.com/p/AF1QipOMzXpKAQNyUvrjTGHqCgWk8spwnzwP8Ml2aDKt=s0",
             location="Centras", has_sockets=True, has_toilet=True, has_wifi=True,
             can_take_calls=False, seats="20-30", coffee_price="€2.50"),

        Cafe(name="Koffee Lab", map_url="https://maps.app.goo.gl/rEyVPaBavCWyKfsb8",
             img_url="https://lh3.googleusercontent.com/p/AF1QipPBAt6bYna7pv5c7e_PhCDPMKPb6oFf6kMT2VQ1=s0",
             location="Vilniaus gatvė", has_sockets=True, has_toilet=False, has_wifi=True,
             can_take_calls=False, seats="0-10", coffee_price="€2.50"),

        Cafe(name="Cafe ORA", map_url="https://maps.app.goo.gl/WkrVQTCM9NXKwapZ9",
             img_url="https://lh3.googleusercontent.com/p/AF1QipM9Dz_QMkOF2da1aNLuTzS_vPvVWBnE84rZLK_G=s0",
             location="Kauno senamiestis", has_sockets=True, has_toilet=True, has_wifi=True,
             can_take_calls=False, seats="20-30", coffee_price="€2.50"),

        Cafe(name="BRUNCH BAR", map_url="https://maps.app.goo.gl/t5UBwqM1PDs8Swxd6",
             img_url="https://lh3.googleusercontent.com/p/AF1QipN-C650VmJ1XZhzOIBTg1bUu3_to_GHpyrmUplt=s0",
             location="Kauno senamiestis", has_sockets=True, has_toilet=True, has_wifi=True,
             can_take_calls=False, seats="20+", coffee_price="€4.00"),

        Cafe(name="Habits Coffee House", map_url="https://maps.app.goo.gl/jwZ7g4FYsfbHUoyr6",
             img_url="https://lh3.googleusercontent.com/p/AF1QipP_NbZH7A1fIQyp5pRm1jOGwzKsDWewaxka6vDt=s0",
             location="Laisvės al.", has_sockets=True, has_toilet=True, has_wifi=True,
             can_take_calls=False, seats="20+", coffee_price="€4.00"),

        Cafe(name="Holy Donut", map_url="https://maps.app.goo.gl/dkZaBBwU7zegZMMT7",
             img_url="https://lh3.googleusercontent.com/p/AF1QipPnOfo7wTICdiAyybF3iFhD3l5aoQjSO-GErma1=s0",
             location="Vilniaus gatvė", has_sockets=True, has_toilet=True, has_wifi=True,
             can_take_calls=False, seats="10-20", coffee_price="€4.00"),

        Cafe(name="Prezo Kepyklele", map_url="https://maps.app.goo.gl/nKqZnhR16wYFLAcm6",
             img_url="https://lh3.googleusercontent.com/p/AF1QipMrdTyRRozGBltwxAseQ4QeuNhbED6meQXlCPsx=s0",
             location="Laisvės al.", has_sockets=True, has_toilet=True, has_wifi=True,
             can_take_calls=True, seats="20-25", coffee_price="€3.10"),

        Cafe(name="101 Kepyklėle", map_url="https://maps.app.goo.gl/pUbMJ23LEVEsyHyu7",
             img_url="https://lh3.googleusercontent.com/p/AF1QipNtHqqIc3kwhpjknrVcMdkhmpA77LDYKmpOJlxf=s0",
             location="Laisvės al.", has_sockets=False, has_toilet=True, has_wifi=True,
             can_take_calls=False, seats="15-20", coffee_price="€2.70"),

        Cafe(name="Kavos Klubas", map_url="https://maps.app.goo.gl/1WcZtJpEzUhtLrBF6",
             img_url="https://lh3.googleusercontent.com/p/AF1QipPyJHFtVzxor4RyQrT-ZEk7ej7OxvmIQYZUHe6G=s0",
             location="Kauno senamiestis", has_sockets=True, has_toilet=True, has_wifi=True,
             can_take_calls=True, seats="20-30", coffee_price="€2.50"),

        Cafe(name="Bōheme House", map_url="https://maps.app.goo.gl/PfzYP4cSdPYzySsn6",
             img_url="https://lh3.googleusercontent.com/p/AF1QipNJQIg-6YTOZhbLu12yGPN3klDxygs7cNAjEo0C=s0",
             location="Kauno senamiestis", has_sockets=True, has_toilet=True, has_wifi=True,
             can_take_calls=False, seats="15-20", coffee_price="€5.00"),

        Cafe(name="Katpėdėlė", map_url="https://maps.app.goo.gl/BhcyCsoohi555GSr5",
             img_url="https://images.adsttc.com/media/images/5014/ec99/28ba/0d58/2800/0d0f/large_jpg/stringio.jpg?1414576924",
             location="MEGA", has_sockets=False, has_toilet=True, has_wifi=True,
             can_take_calls=True, seats="50+", coffee_price="€3.00"),

        Cafe(name="Coco's Café", map_url="https://maps.app.goo.gl/hQMA51ZrmykSPfN48",
             img_url="https://lh3.googleusercontent.com/p/AF1QipOL6jxxpE_D3YS-Zzih61DqNXJKvRIDFiP6ieUI=s0",
             location="Kauno senamiestis", has_sockets=True, has_toilet=True, has_wifi=True,
             can_take_calls=False, seats="20-30", coffee_price="€3.50"),
    ]

    all_cafes = kaunas_cafes

    for cafe in all_cafes:
        db.session.add(cafe)

    db.session.commit()
    print(f"Added {len(all_cafes)} popular cafes from kaunas to the database.")