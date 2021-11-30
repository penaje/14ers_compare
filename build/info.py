selected_peaks = []

peaks_title = {'Whitney': 'Mount Whitney', 'Elbert': 'Mount Elbert', 'Rainier': 'Mount Rainier', 'Denali': 'Denali',
               'Williamson': 'Mount Williamson', 'Shasta': 'Mount Shasta', 'Bierstadt': 'Mount Bierstadt',
               "Handies": "Handies Peak", 'Grays': "Grays Peak", "Quandary": 'Quandary Peak', "Pikes": "Pikes Peak",
               "San_Luis": "San Luis Peak", "White_Mountain": "White Mountain Peak", "Russell": "Mount Russell",
               "Langley": "Mount Langley", "Tyndall": "Mount Tyndall", "Muir": "Mount Muir", 'Split': "Split Mountain",
               'North_Palisade': "North Palisade", "Sill": "Mount Sill", 'Palisade': "Middle Palisade",
               'Sherman': 'Mount Sherman', 'Bross': "Mount Bross", "Lincoln": "Mount Lincoln",
               'Democrat': "Mount Democrat", "Torreys": "Torreys Peak", 'Huron': "Huron Peak",
               "Culebra": "Culebra Peak", "Princeton": "Mount Princeton", "Red_Cloud": "Redcloud Peak",
               'Sunshine': 'Sunshine Peak', 'Evans': "Mount Evans", 'Belford': "Mount Belford",
               "Uncompahgre": "Uncompahgre Peak", 'Shavano': "Mount Shavano", 'Humboldt': "Humboldt Peak",
               'Columbia': "Mount Columbia", 'Yale': "Mount Yale", 'Massive': "Mount Massive", 'Oxford': "Mount Oxford",
               'Antero': "Mount Antero", 'Harvard': "Mount Harvard", 'Capitol': "Capitol Peak", 'Castle': "Castle Peak",
               'Windom': "Windom Peak", 'Challenger': "Challenger Point", 'Blanca': "Blanca Peak",
                'Sneffels': 'Mount Sneffels', 'Lindsey': "Mount Lindsey"



               }

peaks_url = {'Whitney': 'Mount_Whitney', 'Elbert': 'Mount_Elbert', 'Rainier': 'Mount_Rainier', 'Denali': 'Denali',
             'Williamson': "Mount_Williamson", 'Shasta': 'Mount_Shasta', 'Bierstadt': 'Mount_Bierstadt',
             "Handies": "Handies_Peak", "Grays": "Grays_Peak", "Quandary": "Quandary_Peak", "Pikes": "Pikes_Peak",
             "San_Luis": "San_Luis_Peak", "White_Mountain": "White_Mountain_Peak",
             "Russell": "Mount_Russell_(California)", "Langley": "Mount_Langley", "Tyndall": "Mount_Tyndall",
             "Muir": "Mount_Muir", "Split": "Split_Mountain_(California)", "North_Palisade": "North_Palisade",
             'Sill': "Mount_Sill", 'Palisade': "Middle_Palisade", 'Sherman': "Mount_Sherman", 'Bross': "Mount_Bross",
             "Lincoln": "Mount_Lincoln_(Colorado)", "Democrat": "Mount_Democrat", "Torreys": "Torreys_Peak",
             "Huron": "Huron_Peak", "Culebra": "Culebra_Peak", "Princeton": "Mount_Princeton",
             'Red_Cloud': "Redcloud_Peak", 'Sunshine': 'Sunshine_Peak', 'Evans': "Mount_Evans",
             'Belford': "Mount_Belford", "Uncompahgre": "Uncompahgre_Peak", 'Shavano': "Mount_Shavano",
             "Humboldt": 'Humboldt_Peak_(Colorado)', "Columbia": "Mount_Columbia_(Colorado)", 'Yale': "Mount_Yale",
             'Massive': "Mount_Massive", 'Oxford': "Mount_Oxford_(Colorado)", "Antero": "Mount_Antero",
             'Harvard': "Mount_Harvard", 'Capitol': "Capitol_Peak_(Colorado)", 'Castle': "Castle_Peak_(Colorado)",
             'Windom': 'Windom_Peak', 'Challenger': "Challenger_Point", 'Blanca': "Blanca_Peak",
             'Sneffels': "Mount_Sneffels", 'Lindsey': "Mount_Lindsey"




             }

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
                    "Split": "https://www.alltrails.com/trail/us/california/split-mountain--3",
                    "North_Palisade": "https://www.alltrails.com/trail/us/california/north-palisade-via-bishop-pass"
                                      "-trail",
                    'Sill': "https://www.alltrails.com/trail/us/california/mount-sill-via-big-pine-creek-south-fork"
                            "-trail",
                    'Palisade': "https://www.alltrails.com/trail/us/california/middle-palisade",
                    'Sherman': "https://www.alltrails.com/trail/us/colorado/mount-sherman-trail-via-four-mile-creek"
                               "-road ",
                    'Bross': "https://www.alltrails.com/trail/us/colorado/the-decalibron-mounts-democrat-cameron"
                             "-lincoln-and-bross-trail",
                    "Democrat": "https://www.alltrails.com/trail/us/colorado/the-decalibron-mounts-democrat-cameron"
                                "-lincoln-and-bross-trail",
                    "Cameron": "https://www.alltrails.com/trail/us/colorado/the-decalibron-mounts-democrat-cameron"
                               "-lincoln-and-bross-trail",
                    "Lincoln": "https://www.alltrails.com/trail/us/colorado/the-decalibron-mounts-democrat-cameron"
                               "-lincoln-and-bross-trail ",
                    "Torreys": "https://www.alltrails.com/trail/us/colorado/grays-and-torreys-peak",
                    "Huron": "https://www.alltrails.com/trail/us/colorado/huron-peak-via-north-huron-trail",
                    "Culebra": "https://www.alltrails.com/trail/us/colorado/culebra-peak-trail",
                    "Princeton": "https://www.alltrails.com/trail/us/colorado/mount-princeton-trail",
                    'Red_Cloud': "https://www.alltrails.com/trail/us/colorado/redcloud-and-sunshine-peaks",
                    "Sunshine": "https://www.alltrails.com/trail/us/colorado/redcloud-and-sunshine-peaks",
                    'Evans': "https://www.alltrails.com/trail/us/colorado/mount-evans-and-mount-spalding-loop-trail",
                    'Belford': "https://www.alltrails.com/trail/us/colorado/mount-belford",
                    'Uncompahgre': "https://www.alltrails.com/trail/us/colorado/uncompahgre-peak-via-nellie-creek-road",
                    'Shavano': "https://www.alltrails.com/trail/us/colorado/mount-shavano",
                    'Humboldt': "https://www.alltrails.com/trail/us/colorado/humboldt-peak-trail",
                    'Columbia': "https://www.alltrails.com/trail/us/colorado/mt-columbia-southeast-ridge",
                    'Yale': "https://www.alltrails.com/trail/us/colorado/mount-yale-summit-trail",
                    'Massive': "https://www.alltrails.com/trail/us/colorado/mount-massive-trail-via-south-east",
                    'Oxford': "https://www.alltrails.com/trail/us/colorado/mount-oxford-and-belford",
                    'Antero': "https://www.alltrails.com/trail/us/colorado/mount-antero-trail",
                    'Harvard': "https://www.alltrails.com/trail/us/colorado/mount-harvard-trail",
                    'Capitol': "https://www.alltrails.com/trail/us/colorado/capitol-peak",
                    'Castle': 'https://www.alltrails.com/trail/us/colorado/castle-peak--3',
                    'Windom': "https://www.alltrails.com/trail/us/colorado/wisdom-peak-via-needle-creek-trail",
                    "Challenger": "https://www.alltrails.com/trail/us/colorado/challenger-point",
                    'Blanca': "https://www.alltrails.com/trail/us/colorado/blanca-peak",
                    'Sneffels': "https://www.alltrails.com/trail/us/colorado/mount-sneffels-via-blue-lakes-trail",
                    'Lindsey': "https://www.alltrails.com/trail/us/colorado/mount-lindsey-trail",





                    }

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
                            "-california-split-mountain--3-at-map-47960922-1605739601-300x250-1.png ",
                   "North_Palisade": 'https://cdn-assets.alltrails.com/static-map/production/at-map/19130960/trail-us'
                                     '-california-north-palisade-via-bishop-pass-trail-at-map-19130960-1625875368'
                                     '-300x250-1.png ',
                   'Sill': 'https://cdn-assets.alltrails.com/static-map/production/at-map/54593415/trail-us'
                           '-california-mount-sill-via-big-pine-creek-south-fork-trail-at-map-54593415-1602526219'
                           '-300x250-1.png ',
                   'Palisade': "https://cdn-assets.alltrails.com/static-map/production/at-map/21121001/trail-us"
                               "-california-middle-palisade-at-map-21121001-1603313461-300x250-1.png ",
                   'Sherman': "https://cdn-assets.alltrails.com/static-map/production/at-map/46931120/trail-us"
                              "-colorado-mount-sherman-trail-via-four-mile-creek-road-at-map-46931120-1634071924"
                              "-300x250-1.png ",
                   "Bross": "https://cdn-assets.alltrails.com/static-map/production/at-map/75193976/trail-us-colorado"
                            "-the-decalibron-mounts-democrat-cameron-lincoln-and-bross-trail-at-map-75193976"
                            "-1623693563-300x250-1.png ",
                   "Lincoln": "https://cdn-assets.alltrails.com/static-map/production/at-map/75193976/trail-us"
                              "-colorado-the-decalibron-mounts-democrat-cameron-lincoln-and-bross-trail-at-map"
                              "-75193976-1623693563-300x250-1.png ",
                   "Democrat": "https://cdn-assets.alltrails.com/static-map/production/at-map/75193976/trail-us"
                               "-colorado-the-decalibron-mounts-democrat-cameron-lincoln-and-bross-trail-at-map"
                               "-75193976-1623693563-300x250-1.png ",
                   "Torreys": "https://cdn-assets.alltrails.com/static-map/production/at-map/67634252/trail-us"
                              "-colorado-grays-and-torreys-peak-at-map-67634252-1618348298-300x250-1.png ",
                   "Huron": "https://cdn-assets.alltrails.com/static-map/production/at-map/72768410/trail-us-colorado"
                            "-huron-peak-via-north-huron-trail-at-map-72768410-1622218958-300x250-1.png ",
                   "Culebra": "https://cdn-assets.alltrails.com/static-map/production/at-map/21245390/trail-us"
                              "-colorado-culebra-peak-trail-at-map-21245390-1590528102-300x250-1.png ",
                   "Princeton": "https://cdn-assets.alltrails.com/static-map/production/at-map/13269572/trail-us"
                                "-colorado-mount-princeton-trail-at-map-13269572-1627683433-300x250-1.png ",
                   "Red_Cloud": "https://cdn-assets.alltrails.com/static-map/production/at-map/27179112/trail-us"
                                "-colorado-redcloud-and-sunshine-peaks-at-map-27179112-1590529525-300x250-1.png ",
                   'Sunshine': "https://cdn-assets.alltrails.com/static-map/production/at-map/27179112/trail-us"
                               "-colorado-redcloud-and-sunshine-peaks-at-map-27179112-1590529525-300x250-1.png ",
                   'Evans': "https://cdn-assets.alltrails.com/static-map/production/at-map/88322646/trail-us-colorado"
                            "-mount-evans-and-mount-spalding-loop-trail-at-map-88322646-1631818809-300x250-1.png ",
                   'Belford': "https://cdn-assets.alltrails.com/static-map/production/at-map/83158052/trail-us"
                              "-colorado-mount-belford-at-map-83158052-1628540314-300x250-1.png ",
                   'Uncompahgre': "https://cdn-assets.alltrails.com/static-map/production/at-map/21247012/trail-us"
                                  "-colorado-uncompahgre-peak-via-nellie-creek-road-at-map-21247012-1627539647"
                                  "-300x250-1.png ",
                   "Shavano": "https://cdn-assets.alltrails.com/static-map/production/at-map/29483675/trail-us"
                              "-colorado-mount-shavano-at-map-29483675-1590530891-300x250-1.png ",
                   'Humboldt': "https://cdn-assets.alltrails.com/static-map/production/at-map/20683730/trail-us"
                               "-colorado-humboldt-peak-trail-at-map-20683730-1590531613-300x250-1.png ",
                   'Columbia': "https://cdn-assets.alltrails.com/static-map/production/at-map/18035691/trail-us"
                               "-colorado-mt-columbia-southeast-ridge-at-map-18035691-1590514636-300x250-1.png",
                   'Yale': "https://cdn-assets.alltrails.com/static-map/production/at-map/18115874/trail-us-colorado"
                           "-mount-yale-summit-trail-at-map-18115874-1590529756-300x250-1.png ",
                   'Massive': "https://cdn-assets.alltrails.com/static-map/production/at-map/13353839/trail-us"
                              "-colorado-mount-massive-trail-via-south-east-at-map-13353839-1592348840-300x250-1.png ",
                   'Oxford': "https://cdn-assets.alltrails.com/static-map/production/at-map/49177954/trail-us"
                             "-colorado-mount-oxford-and-belford-at-map-49177954-1597767832-300x250-1.png ",
                   "Antero": "https://cdn-assets.alltrails.com/static-map/production/at-map/85348635/trail-us"
                             "-colorado-mount-antero-trail-at-map-85348635-1629903761-300x250-1.png ",
                   'Harvard':"https://cdn-assets.alltrails.com/static-map/production/at-map/27172955/trail-us"
                             "-colorado-mount-harvard-trail-at-map-27172955-1629050647-300x250-1.png ",
                   'Capitol': 'https://cdn-assets.alltrails.com/static-map/production/at-map/23397582/trail-us'
                              '-colorado-capitol-peak-at-map-23397582-1590524636-300x250-1.png ',
                   'Castle': "https://cdn-assets.alltrails.com/static-map/production/at-map/21245092/trail-us"
                             "-colorado-castle-peak--3-at-map-21245092-1627107836-300x250-1.png ",
                   'Windom': "https://cdn-assets.alltrails.com/static-map/production/at-map/21244606/trail-us"
                             "-colorado-wisdom-peak-via-needle-creek-trail-at-map-21244606-1626933680-300x250-1.png ",
                   'Challenger': "https://cdn-assets.alltrails.com/static-map/production/at-map/21236669/trail-us"
                                 "-colorado-challenger-point-at-map-21236669-1590528084-300x250-1.png",
                   'Blanca': "https://cdn-assets.alltrails.com/static-map/production/at-map/13294034/trail-us"
                             "-colorado-blanca-peak-at-map-13294034-1599169773-300x250-1.png ",
                   'Sneffels': "https://cdn-assets.alltrails.com/static-map/production/at-map/50460794/trail-us"
                               "-colorado-mount-sneffels-via-blue-lakes-trail-at-map-50460794-1619732955-300x250-1.png "
                   , 'Lindsey': "https://cdn-assets.alltrails.com/static-map/production/at-map/89146217/trail-us"
                                "-colorado-mount-lindsey-trail-at-map-89146217-1632155512-300x250-1.png "



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
                    "Challenger": "https://www.peakbagger.com/peak.aspx?pid=5902",
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
                    "Red_Cloud": "https://www.peakbagger.com/peak.aspx?pid=5847",
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
