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

peaks_dict = {"Whitney": "Mount Whitney, of the California Sierra Nevada, holds numerous distinctions. It is the "
                         "highpoint of both Tulare & Inyo counties. It is the highest peak in the Sierra, & indeed in "
                         "all of California. Finally, it rises higher than any piece of land in the United States "
                         "outside of Alaska. "

                         "Mount Whitney's elevation stature continues to intrigue the human psyche, both from a "
                         "civilian as well as a "
                         "governmental perspective. Its elevation seems to be continually evaluated and reevaluated "
                         "using the newest technologies, perpetually changing (usually in an upward trend) the "
                         "mountain's height. The NPS plaque on the mountain lists Whitney's official height at 14,"
                         "496.811 feet. The most recent observations by NGS (National Geodetic Survey)/NOAA (National "
                         "Oceanographic & Atmospheric Administration) put it at 14,505' (4,421m)- thanks Eleutheros! "

                         "All this being said, it is still no 5,000m (let alone 6,000 or 7,000m) peak. It would be a "
                         "minor (if somewhat steep "
                         "on certain aspects) foothill in any of the Earth’s great ranges. It harbors no glaciers. A "
                         "huge number of people, possessing little wilderness skills or technical expertise, "
                         "manage to run, hike, &/or crawl their way to the top of this large piece of exposed granite "
                         "each year via the uninspiring Mt. Whitney trail. "

                         "The attributes which make Mt. Whitney a truly great mountain are frequently overlooked. "
                         "History, commanding "
                         "position, excellent rock, its great east face & ‘subsidiary’ needles, & a tantalizing "
                         "selection of routes are arguably the bread & butter of Mt. Whitney. During the winter "
                         "months, delightful opportunities also exist for the ski mountaineer / backcountry "
                         "snowboarder. "

                         "While its gentle western slopes would hardly inspire the hardened mountaineer, Whitney’s "
                         "east face, erupting 2, "
                         "000 ft. above cold & serene Iceberg Lake, draws the climber’s eye upward & makes them "
                         "yearn. Whitney’s subsidiary needles, (to the south of the main east face), "
                         "are awe-inspiring enough by themselves, & have their own epics, legends, & lore firmly "
                         "established. "

                         "The proximity of the highest point in the continental US with the lowest point in North "
                         "America has not escaped "
                         "notice. The Badwater Ultramarathon, begun officially in 1987, takes some of the most "
                         "masochistic individuals imaginable from Badwater (Death Valley) to the lofty summit of Mt. "
                         "Whitney. Before this was ‘en vogue,’ Stan Rodefer and Jim Burnworth of San Diego became the "
                         "first people to do the Badwater/Whitney (Lowest/Highest) hike in recorded history, "
                         "in October 1969. They took 2 weeks, crossed the dreaded salt flats and hiked a direct route "
                         "not using roads or any other conveniences (this was documented by the Park Rangers and in a "
                         "November 4, 1969 San Diego Tribune article entitled 'Hikers View High, Low Sites in the "
                         "U.S.'). Props. Ouch. "

                         "The 11-mile Mount Whitney Trail (class 1) is the easiest and most popular route to the "
                         "summit and is often done as a "
                         "strenuous 22-mile day hike. During the summer and autumn months, only sneakers are "
                         "necessary to ascend this summit from the Whitney Portal trailhead at 8,365 feet, however, "
                         "earlier in the season, an ice axe and crampons may be required. Many people will appreciate "
                         "taking two days to do this hike, spending a night at Outpost Camp or Trail Camp. An "
                         "interesting time to visit is the month of April, before the quota season starts, "
                         "when the snowpack is firmer and Trail Camp becomes a base camp for groups hanging out in "
                         "the winter alpine scenery using their 2-way radios to talk to those above Trail Crest. "

                         "While there are many other routes on Whitney, the most popular ones after the main trail "
                         "include: the Mountaineer's "
                         "Route, East Face, East Buttress, and North Slope. The first three of these start from "
                         "Iceberg Lake while the last one is often climbed as a traverse from Mount Russell. Winter "
                         "makes the Mountaineer's Route a popular objective. The East Face & East Buttress are the "
                         "classic technical climbs on the peak.",
              'Rainier': 'All climbing routes on Mount Rainier require climbers to possess some level of technical '
                         'climbing skill. This includes ascending and descending the mountain with the use of '
                         'technical climbing equipment such as crampons, ice axes, harnesses, and ropes. Difficulty '
                         'and technical challenge of climbing Mount Rainier can vary widely between climbing routes. '
                         'Routes are graded in NCCS Alpine Climbing format.',
              'Elbert': "There are three main routes to ascend the mountain, all of which gain over 4,100 feet (1,"
                        "200 m) elevation. The standard route ascends the peak from the east, starting from the "
                        "Colorado Trail just north of Twin Lakes. The 4.6 miles (7.4 km) long North (Main) Elbert "
                        "Trail begins close to the Elbert Creek Campground, and gains about 4,500 feet (1,"
                        "400 m).[20][21] The trail is open to equestrians, mountain bikers and hunters during "
                        "season.[22] An easier, but longer route, the South Elbert Trail, is 5.5 miles (8.9 km) long, "
                        "climbing 4,600 feet (1,400 m) at a less-punishing gradient than the North Elbert Trail, "
                        "approaching from the south and then climbing the eastern ridge.",
              'Denali': 'No Climbing Routes Data Available, Please Seek Other Resources',
              'Williamson': "The standard ascent route is the West Side Route, accessed from Shepherd's Pass. From "
                            "the pass, one travels across the Williamson Bowl, which lies between Mount Williamson "
                            "and Mount Tyndall, part of the Sierra Crest. The bowl is home to five high alpine lakes. "
                            "From the bowl, the route climbs gullies up the west face to the relatively broad summit "
                            "plateau; this portion involves scrambling up to class 3. Technically easier, but with a "
                            "more difficult approach which can involve route finding and bushwhacking, "
                            "is the Southeast Slopes Route, rising from George Creek. Other routes exist on the "
                            "mountain, including a significant technical route on the North Rib",
              'Shasta': "The most popular route on Mount Shasta is Avalanche Gulch route, which begins at the Bunny "
                        "Flat Trailhead and gains about 7,300 feet (2,200 m) of elevation in a round trip of "
                        "approximately 11.5 miles (18.5 km). The crux of this route is considered to be to climb from "
                        "Lake Helen, at approximately 10,443 feet (3,183 m), to the top of Red Banks. The Red Banks "
                        "are the most technical portion of the climb, as they are usually full of snow and ice, "
                        "are very steep, and top out at around 13,000 feet (4,000 m) before the route heads to Misery "
                        "Hill.[39] The Casaval Ridge route is a steeper, more technical route on the mountain's "
                        "southwest ridge best climbed when there is a lot of snow pack. This route tops out to the "
                        "left (north) of the Red Banks, directly west of Misery Hill. So the final sections involve a "
                        "trudge up Misery Hill to the summit plateau, similar to the Avalanche Gulch route ",
              'Bierstadt': "Mount Bierstadt is located 1.4 miles (2.2 km) west by south of Mount Evans and 43.8 miles "
                           "(70.5 km) west by south of downtown Denver. "

                           "Because it is generally considered an easy climb, along with its accessibility from "
                           "nearby Denver, Mount Bierstadt "
                           "is one of the most popular mountains to climb in Colorado. As with most peaks in "
                           "Colorado, July and August make the best months for climbing Mount Bierstadt. "

                           "The most popular base from which to begin ascent of Mount Bierstadt is Guanella Pass, "
                           "located to the west. From "
                           "Guanella Pass it is approximately a 7 miles (11 km) hike, with a climb of 2,391 feet (729 "
                           "m). The trail descends slightly into the fairly level marshlands surrounding Scott Gomer "
                           "Creek before reaching Bierstadt's western slopes. On the rocky upper regions of the "
                           "mountain the route of the trail is marked by a series of cairns. The trail levels about "
                           "200 feet (61 m) below the summit at saddle point before beginning the final ascent. "
                           "Alternative trails cover the eastern slopes for longer hikes. "

                           "Once at the summit, a popular option is to continue the hike to nearby Mount Evans along "
                           "a ridge known as The Sawtooth, an intermediate-level hike that overlooks Abyss Lake, "
                           "which occupies the bottom of the valley separating Bierstadt and Evans. "
              }
