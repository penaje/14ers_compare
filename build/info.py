selected_peaks = []

peaks_title = {'Whitney': 'Mount Whitney', 'Elbert': 'Mount Elbert', 'Rainier': 'Mount Rainier', 'Denali': 'Denali',
               'Williamson': 'Mount Williamson', 'Shasta': 'Mount Shasta', 'Bierstadt': 'Mount Bierstadt',
               "Handies": "Handies Peak", 'Grays': "Grays Peak", "Quandary": 'Quandary Peak', "Pikes": "Pikes Peak",
               "San_Luis": "San Luis Peak", "White_Mountain": "White Mountain Peak", "Russell": "Mount Russell",
               "Langley": "Mount Langley", "Tyndall": "Mount Tyndall", "Muir": "Mount Muir", 'Split': "Split Mountain"}

peaks_url = {'Whitney': 'Mount_Whitney', 'Elbert': 'Mount_Elbert', 'Rainier': 'Mount_Rainier', 'Denali': 'Denali',
             'Williamson': "Mount_Williamson", 'Shasta': 'Mount_Shasta', 'Bierstadt': 'Mount_Bierstadt',
             "Handies": "Handies_Peak", "Grays": "Grays_Peak", "Quandary": "Quandary_Peak", "Pikes": "Pikes_Peak",
             "San_Luis": "San_Luis_Peak", "White_Mountain": "White_Mountain_Peak",
             "Russell": "Mount_Russell_(California)", "Langley": "Mount_Langley", "Tyndall": "Mount_Tyndall",
             "Muir": "Mount_Muir", "Split": "Split_Mountain_(California)"}

all_trails_links = {'Shasta': "https://www.alltrails.com/trail/us/california/mount-shasta-via-avalanche-gulch-route",
                    'Whitney': "https://www.alltrails.com/trail/us/california/mount-whitney-via-mount-whitney-trail",
                    'Elbert': "https://www.alltrails.com/trail/us/colorado/north-mount-elbert-trail--3",
                    'Bierstadt': "https://www.alltrails.com/trail/us/colorado/mount-bierstadt-trail",
                    "Rainier": "https://www.alltrails.com/trail/us/washington/mount-rainier-standard-summit-route",
                    "Denali": "https://www.alltrails.com/trail/us/alaska/denali-viewpoint-south",
                    "Handies": "https://www.alltrails.com/trail/us/colorado/handies-peak",
                    "Grays": "https://www.alltrails.com/trail/us/colorado/grays-peak--3",
                    "Quandary": "https://www.alltrails.com/trail/us/colorado/quandary-peak-trail",
                    "Pikes": "https://www.alltrails.com/trail/us/colorado/pikes-peak-via-barr-trail--2",
                    "San_Luis": "https://www.alltrails.com/trail/us/colorado/san-luis-summit",
                    "White_Mountain": "https://www.alltrails.com/trail/us/california/white-mountain-peak",
                    "Russell": "https://www.alltrails.com/trail/us/california/mount-russell-from-ravine-campground",
                    "Langley": "https://www.alltrails.com/trail/us/california/mount-langley",
                    "Tyndall": "https://www.alltrails.com/trail/us/california/mount-tyndall-trail",
                    "Muir": "https://www.alltrails.com/trail/us/california/mount-muir-via-the-mount-whitney-trail",
                    "Split": "https://www.alltrails.com/trail/us/california/split-mountain--3"}

all_trails_maps = {'Shasta': "https://cdn-assets.alltrails.com/static-map/production/at-map/13576197/trail-us"
                             "-california-mount-shasta-via-avalanche-gulch-route-at-map-13576197-1590536269-300x250-1"
                             ".png",
                   'Whitney': "https://cdn-assets.alltrails.com/static-map/production/at-map/69203534/trail-us"
                              "-california-mount-whitney-via-mount-whitney-trail-at-map-69203534-1619646787-300x250-1"
                              ".png",
                   'Elbert': "https://cdn-assets.alltrails.com/static-map/production/at-map/80125290/trail-us"
                             "-colorado-north-mount-elbert-trail--3-at-map-80125290-1626784161-300x250-1.png",
                   "Bierstadt": "https://cdn-assets.alltrails.com/static-map/production/at-map/81048638/trail-us"
                                "-colorado-mount-bierstadt-trail-at-map-81048638-1627313769-300x250-1.png",
                   "Rainier": "https://cdn-assets.alltrails.com/static-map/production/at-map/20075622/trail-us"
                              "-washington-mount-rainier-standard-summit-route-at-map-20075622-1605912675-300x250-1"
                              ".png",
                   "Denali": "https://cdn-assets.alltrails.com/static-map/production/at-map/70685631/trail-us-alaska"
                             "-denali-viewpoint-south-at-map-70685631-1620755998-300x250-1.png",
                   "Handies": "https://cdn-assets.alltrails.com/static-map/production/at-map/14133285/trail-us"
                              "-colorado-handies-peak-at-map-14133285-1590529022-300x250-1.png",
                   "Grays": "https://cdn-assets.alltrails.com/static-map/production/at-map/28334499/trail-us-colorado"
                            "-grays-peak--3-at-map-28334499-1590529545-300x250-1.png",
                   "Quandary": "https://cdn-assets.alltrails.com/static-map/production/at-map/69208263/trail-us"
                               "-colorado-quandary-peak-trail-at-map-69208263-1627160319-300x250-1.png",
                   "Pikes": "https://cdn-assets.alltrails.com/static-map/production/at-map/68281804/trail-us-colorado"
                            "-pikes-peak-via-barr-trail--2-at-map-68281804-1634764532-300x250-1.png",
                   "San_Luis": "https://cdn-assets.alltrails.com/static-map/production/at-map/21248320/trail-us"
                               "-colorado-san-luis-summit-at-map-21248320-1630184829-300x250-1.png",
                   "White_Mountain": "https://cdn-assets.alltrails.com/static-map/production/at-map/46020127/trail-us"
                                     "-california-white-mountain-peak-from-locked-gate--3-at-map-46020127-1593972956"
                                     "-300x250-1.png ",
                   "Russell": "https://cdn-assets.alltrails.com/static-map/production/at-map/50073955/trail-us"
                              "-california-mount-russell-from-ravine-campground-at-map-50073955-1627841111-300x250-1"
                              ".png ",
                   "Langley": "https://cdn-assets.alltrails.com/static-map/production/at-map/48677911/trail-us"
                              "-california-mount-langley-at-map-48677911-1605917706-300x250-1.png ",
                   "Tyndall": "https://cdn-assets.alltrails.com/static-map/production/at-map/46326352/trail-us"
                              "-california-mount-tyndall-trail-at-map-46326352-1605919944-300x250-1.png ",
                   "Muir": "https://cdn-assets.alltrails.com/static-map/production/at-map/13285854/trail-us"
                           "-california-mount-muir-via-the-mount-whitney-trail-at-map-13285854-1627841097-300x250-1"
                           ".png ",
                   "Split": "https://cdn-assets.alltrails.com/static-map/production/at-map/47960922/trail-us"
                            "-california-split-mountain--3-at-map-47960922-1605739601-300x250-1.png "

                   }

peak_bagger_urls = {"Massive": "https://www.peakbagger.com/peak.aspx?pid=5729",
                    "Denali": "https://www.peakbagger.com/peak.aspx?pid=271",
                    "Elbert": "https://www.peakbagger.com/peak.aspx?pid=5736",
                    "Harvard": "https://www.peakbagger.com/peak.aspx?pid=5754",
                    "Blanca": "https://www.peakbagger.com/peak.aspx?pid=5921",
                    "La_Plata": "https://www.peakbagger.com/peak.aspx?pid=5744",
                    "Uncompahgre": "https://www.peakbagger.com/peak.aspx?pid=5836",
                    "Crestone": "https://www.peakbagger.com/peak.aspx?pid=5908",
                    "Lincoln": "https://www.peakbagger.com/peak.aspx?pid=5793",
                    "Grays": "https://www.peakbagger.com/peak.aspx?pid=5664",
                    "Antero": "https://www.peakbagger.com/peak.aspx?pid=5759",
                    "Torreys": "https://www.peakbagger.com/peak.aspx?pid=5662",
                    "Castle": "https://www.peakbagger.com/peak.aspx?pid=5709",
                    "Quandary": "https://www.peakbagger.com/peak.aspx?pid=5788",
                    "Evans": "https://www.peakbagger.com/peak.aspx?pid=5676",
                    "Longs": "https://www.peakbagger.com/peak.aspx?pid=5642",
                    "Mt_Wilson": "https://www.peakbagger.com/peak.aspx?pid=5820",
                    "Cameron": "https://www.peakbagger.com/peak.aspx?pid=5794",
                    "Shavano": "https://www.peakbagger.com/peak.aspx?pid=5762",
                    "Princeton": "https://www.peakbagger.com/peak.aspx?pid=5757",
                    "Belford": "https://www.peakbagger.com/peak.aspx?pid=5747",
                    "Yale": "https://www.peakbagger.com/peak.aspx?pid=5756",
                    "Bross": "https://www.peakbagger.com/peak.aspx?pid=5796",
                    "Kit_Carson": "https://www.peakbagger.com/peak.aspx?pid=5903",
                    "El_Diente": "https://www.peakbagger.com/peak.aspx?pid=5819",
                    "Maroon": "https://www.peakbagger.com/peak.aspx?pid=5701",
                    "Tabeguache": "https://www.peakbagger.com/peak.aspx?pid=5761",
                    "Oxford": "https://www.peakbagger.com/peak.aspx?pid=5746",
                    "Sneffels": "https://www.peakbagger.com/peak.aspx?pid=5830",
                    "Democrat": "https://www.peakbagger.com/peak.aspx?pid=5795",
                    "Capitol": "https://www.peakbagger.com/peak.aspx?pid=5695",
                    "Pikes": "https://www.peakbagger.com/peak.aspx?pid=5689",
                    "Snowmass": "https://www.peakbagger.com/peak.aspx?pid=5697",
                    "Windom": "https://www.peakbagger.com/peak.aspx?pid=5861",
                    "Eolus": "https://www.peakbagger.com/peak.aspx?pid=5860",
                    "Challenger Point": "https://www.peakbagger.com/peak.aspx?pid=5902",
                    "Columbia": "https://www.peakbagger.com/peak.aspx?pid=5755",
                    "Missouri": "https://www.peakbagger.com/peak.aspx?pid=5748",
                    "Humboldt": "https://www.peakbagger.com/peak.aspx?pid=5906",
                    "Bierstadt": "https://www.peakbagger.com/peak.aspx?pid=5678",
                    "Sunlight": "https://www.peakbagger.com/peak.aspx?pid=5858",
                    "Handies": "https://www.peakbagger.com/peak.aspx?pid=5840",
                    "Culebra": "https://www.peakbagger.com/peak.aspx?pid=5924",
                    "Lindsey": "https://www.peakbagger.com/peak.aspx?pid=5918",
                    "Ellingwood": "https://www.peakbagger.com/peak.aspx?pid=5919",
                    "Conundrum": "https://www.peakbagger.com/peak.aspx?pid=16693",
                    "North_Eolus": "https://www.peakbagger.com/peak.aspx?pid=5859",
                    "Little_Bear": "https://www.peakbagger.com/peak.aspx?pid=5922",
                    "Sherman": "https://www.peakbagger.com/peak.aspx?pid=5803",
                    "Redcloud": "https://www.peakbagger.com/peak.aspx?pid=5847",
                    "Pyramid": "https://www.peakbagger.com/peak.aspx?pid=5700",
                    "Wilson_Peak": "https://www.peakbagger.com/peak.aspx?pid=5816",
                    "Wetterhorn": "https://www.peakbagger.com/peak.aspx?pid=5838",
                    "San_Luis": "https://www.peakbagger.com/peak.aspx?pid=5874",
                    "North_Maroon": "https://www.peakbagger.com/peak.aspx?pid=5699",
                    "Mount_of_the_Holy_Cross": "https://www.peakbagger.com/peak.aspx?pid=5725",
                    "Huron": "https://www.peakbagger.com/peak.aspx?pid=5749",
                    "Sunshine": "https://www.peakbagger.com/peak.aspx?pid=5848",
                    "Whitney": "https://www.peakbagger.com/peak.aspx?pid=2829",
                    "Williamson": "https://www.peakbagger.com/peak.aspx?pid=2814",
                    "White_Mountain": "https://www.peakbagger.com/peak.aspx?pid=3628",
                    "North_Palisade": "https://www.peakbagger.com/peak.aspx?pid=2727",
                    "Shasta": "https://www.peakbagger.com/peak.aspx?pid=2477",
                    "Sill": "https://www.peakbagger.com/peak.aspx?pid=2726",
                    "Russell": "https://www.peakbagger.com/peak.aspx?pid=2826",
                    "Split": "https://www.peakbagger.com/peak.aspx?pid=2738",
                    "Langley": "https://www.peakbagger.com/peak.aspx?pid=2845",
                    "Tyndall": "https://www.peakbagger.com/peak.aspx?pid=2815",
                    "Palisade": "https://www.peakbagger.com/peak.aspx?pid=2732",
                    "Muir": "https://www.peakbagger.com/peak.aspx?pid=2832",
                    'Rainier': "https://www.peakbagger.com/peak.aspx?pid=2296"}
