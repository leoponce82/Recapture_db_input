class Trap:
    def __init__(
        self,
        country,
        province,
        county,
        location,
        long,
        latt,
        altitude,
        trap_code,
        trap_methods,
        trap_installation_date,
        release_date,
        release_time,
        collection_date,
        collection_time,
        temperature,
        humidity,
        AEG_pink_male,
        AEG_pink_female,
        AEG_yellow_male,
        AEG_yellow_female,
        AEG_nomarked_male,
        AEG_nomarked_female,
        CUX_nomarked_male,
        CUX_nomarked_female,
        taenorhincus_nomarked_male,
        taenorhincus_nomarked_female,
        OBS,
    ):
        self.country = country
        self.province = province
        self.county = county
        self.location = location
        self.long = long
        self.latt = latt
        self.altitude = altitude
        self.trap_code = trap_code
        self.trap_methods = trap_methods
        self.trap_installation_date = trap_installation_date
        self.release_date = release_date
        self.release_time = release_time
        self.collection_date = collection_date
        self.collection_time = collection_time
        self.temperature = temperature
        self.humidity = humidity
        self.AEG_pink_male = AEG_pink_male
        self.AEG_pink_female = AEG_pink_female
        self.AEG_yellow_male = AEG_yellow_male
        self.AEG_yellow_female = AEG_yellow_female
        self.AEG_nomarked_male = AEG_nomarked_male
        self.AEG_nomarked_female = AEG_nomarked_female
        self.CUX_nomarked_male = CUX_nomarked_male
        self.CUX_nomarked_female = CUX_nomarked_female
        self.taenorhincus_nomarked_male = taenorhincus_nomarked_male
        self.taenorhincus_nomarked_female = taenorhincus_nomarked_female
        self.OBS = OBS
