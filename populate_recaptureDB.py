import sqlite3

conn = sqlite3.connect("recapture.db")

c = conn.cursor()

c.execute(
    """CREATE TABLE recapture (
        country text,
        province text,
        county text,
        location text,
        long text,
        latt text,
        altitude real,
        trap_code text,
        trap_methods text,
        trap_installation_date text,
        release_date text,
        release_time text,
        collection_date text,
        collection_time text,
        temperature real,
        humidity real,
        AEG_pink_male integer,
        AEG_pink_female integer,
        AEG_yellow_male integer,
        AEG_yellow_female integer,
        AEG_nomarked_male integer,
        AEG_nomarked_female integer,
        CUX_nomarked_male integer,
        CUX_nomarked_female integer,
        taenorhincus_nomarked_male integer,
        taenorhincus_nomarked_female integer,
        OBS text
        )"""
)

c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-1','BG-SENTINEL','09.03.23','10.03.23','05:30','11.03.23','16:30',NULL,NULL,'0','0','0','0','0','0','0','0','0','0',NULL)")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-2','BG-SENTINEL','09.03.23','10.03.23','05:30','11.03.23','16:30',NULL,NULL,'0','0','0','0','0','0','0','0','0','0',NULL)")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-3','BG-SENTINEL','09.03.23','10.03.23','05:30','11.03.23','16:30',NULL,NULL,'0','0','1','0','1','1','0','0','0','0',NULL)")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-4','BG-SENTINEL','09.03.23','10.03.23','05:30','11.03.23','16:30',NULL,NULL,'0','0','25','1','3','3','5','2','0','0',NULL)")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-5','BG-SENTINEL','09.03.23','10.03.23','05:30','11.03.23','16:30',NULL,NULL,'1','0','7','0','6','2','0','0','0','0',NULL)")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-6','BG-SENTINEL','09.03.23','10.03.23','05:30','11.03.23','16:30',NULL,NULL,'1','0','1','0','0','0','0','0','0','0',NULL)")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-7','BG-SENTINEL','09.03.23','10.03.23','05:30','11.03.23','16:30',NULL,NULL,'0','0','0','0','0','0','0','0','0','0',NULL)")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-8','BG-SENTINEL','09.03.23','10.03.23','05:30',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Esta fecha no se puso trampa en este punto, no habia nadie en la casa')")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-9','BG-SENTINEL','09.03.23','10.03.23','05:30','11.03.23','16:30',NULL,NULL,'0','0','0','0','1','5','0','0','0','0',NULL)")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-10','BG-SENTINEL','09.03.23','10.03.23','05:30','11.03.23','16:30',NULL,NULL,'0','0','1','0','1','7','0','0','0','0',NULL)")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-11','BG-SENTINEL','09.03.23','10.03.23','05:30','11.03.23','16:30',NULL,NULL,'0','0','0','0','0','0','0','0','0','0',NULL)")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-12','BG-SENTINEL','09.03.23','10.03.23','05:30','11.03.23','16:30',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'NO recuperada, no habia nadie en la casa')")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-13','BG-SENTINEL','09.03.23','10.03.23','05:30','11.03.23','16:30',NULL,NULL,'0','0','40','1','3','3','0','8','0','0',NULL)")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-14','BG-SENTINEL','09.03.23','10.03.23','05:30','11.03.23','16:30',NULL,NULL,'1','0','8','0','3','0','2','2','0','0',NULL)")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-15','BG-SENTINEL','09.03.23','10.03.23','05:30','11.03.23','16:30',NULL,NULL,'0','0','0','0','3','0','0','0','0','0',NULL)")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-16','BG-SENTINEL','09.03.23','10.03.23','05:30','11.03.23','16:30',NULL,NULL,'0','0','0','0','0','0','0','0','0','0',NULL)")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-17','BG-SENTINEL','09.03.23','10.03.23','05:30',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'En este punto no se puso trampa, porque un punto esta muy cerca.')")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-18','BG-SENTINEL','09.03.23','10.03.23','05:30','11.03.23','16:30',NULL,NULL,'0','0','2','0','0','0','2','0','0','0',NULL)")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-19','BG-SENTINEL','09.03.23','10.03.23','05:30','11.03.23','16:30',NULL,NULL,'0','0','0','0','0','0','0','0','0','0',NULL)")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-20','BG-SENTINEL','09.03.23','10.03.23','05:30','11.03.23','16:30',NULL,NULL,'0','0','1','0','0','2','0','0','0','0',NULL)")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-21','BG-SENTINEL','09.03.23','10.03.23','05:30','11.03.23','16:30',NULL,NULL,'0','0','3','0','2','2','11','3','0','0',NULL)")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-22','BG-SENTINEL','09.03.23','10.03.23','05:30','11.03.23','16:30',NULL,NULL,'0','0','0','0','2','3','1','0','0','0',NULL)")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-23','BG-SENTINEL','09.03.23','10.03.23','05:30','11.03.23','16:30',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'NO recuperada, no habia nadie en la casa')")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-24','BG-SENTINEL','09.03.23','10.03.23','05:30',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Esta fecha no se puso trampa en este punto, no habia nadie en la casa')")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-25','BG-SENTINEL','09.03.23','10.03.23','05:30','11.03.23','16:30',NULL,NULL,'0','0','5','0','1','0','2','5','0','0',NULL)")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-26','BG-SENTINEL','09.03.23','10.03.23','05:30','11.03.23','16:30',NULL,NULL,'20','1','0','0','2','2','1','2','0','1',NULL)")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-27','BG-SENTINEL','09.03.23','10.03.23','05:30','11.03.23','16:30',NULL,NULL,'5','0','1','0','0','1','2','0','0','0',NULL)")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-28','BG-SENTINEL','09.03.23','10.03.23','05:30','11.03.23','16:30',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'NO recuperada, no habia nadie en la casa')")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-29','BG-SENTINEL','09.03.23','10.03.23','05:30','11.03.23','16:30',NULL,NULL,'1','0','0','0','3','0','0','1','0','0',NULL)")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-30','BG-SENTINEL','09.03.23','10.03.23','05:30','11.03.23','16:30',NULL,NULL,'0','0','0','0','5','2','6','2','0','0',NULL)")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-31','BG-SENTINEL','09.03.23','10.03.23','05:30','11.03.23','16:30',NULL,NULL,'0','0','1','0','1','2','4','2','0','0',NULL)")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-32','BG-SENTINEL','09.03.23','10.03.23','05:30','11.03.23','16:30',NULL,NULL,'0','0','0','0','3','2','5','2','0','0',NULL)")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-33','BG-SENTINEL','09.03.23','10.03.23','05:30','11.03.23','16:30',NULL,NULL,'0','0','1','0','0','3','0','3','0','0',NULL)")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-34','BG-SENTINEL','09.03.23','10.03.23','05:30','11.03.23','16:30',NULL,NULL,'0','0','0','0','0','0','0','0','0','0',NULL)")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-35','BG-SENTINEL','09.03.23','10.03.23','05:30',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'En este punto no se puso trampa, porque un punto esta muy cerca.')")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-36','BG-SENTINEL','09.03.23','10.03.23','05:30','11.03.23','16:30',NULL,NULL,'0','0','0','0','19','9','2','4','0','0',NULL)")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-37','BG-SENTINEL','09.03.23','10.03.23','05:30','11.03.23','16:30',NULL,NULL,'0','0','0','0','0','0','1','2','0','0',NULL)")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-38','BG-SENTINEL','09.03.23','10.03.23','05:30','11.03.23','16:30',NULL,NULL,'0','0','0','0','0','0','0','0','0','0',NULL)")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-39','BG-SENTINEL','09.03.23','10.03.23','05:30','11.03.23','16:30',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'NO recuperada, no habia nadie en la casa')")
c.execute(" INSERT INTO recapture VALUES ('Ecuador','Galapagos','Santa Cruz','Bellavista',NULL,NULL,NULL,'BG-40','BG-SENTINEL','09.03.23','10.03.23','05:30','11.03.23','16:30',NULL,NULL,'1','0','2','0','0','3','0','0','0','0',NULL)")

conn.commit()

conn.close()

