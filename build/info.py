selected_peaks = []

peaks_title = {'Whitney': 'Mt. Whitney', 'Elbert': 'Mt. Elbert', 'Rainier': 'Mt. Rainier', 'Denali': 'Denali',
               'Williamson': 'Mt. Williamson', 'Shasta': 'Mt. Shasta'}

peaks_url = {'Whitney': 'Mount_Whitney', 'Elbert': 'Mount_Elbert', 'Rainier': 'Mount_Rainier', 'Denali': 'Denali',
             'Williamson': "Mount_Williamson", 'Shasta': 'Mount_Shasta'}

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
                        "trudge up Misery Hill to the summit plateau, similar to the Avalanche Gulch route "
              }
peaks_elevation = {'Whitney': '14,505 ft', 'Elbert': '14,440 ft', 'Rainier': '14,411 ft', 'Denali': '20,310 ft',
                   'Williamson': '14,379 ft', 'Shasta': '14,179 ft'}

peaks_prominence = {'Whitney': '10,075 ft', 'Elbert': '9,093 ft', 'Rainier': '13,210 ft', 'Denali': '20,194 ft',
                    'Williamson': '1,643 ft', 'Shasta': '9,772 ft'}

peaks_isolation = {'Whitney': '1,647 mi', 'Elbert': '671 mi', 'Rainier': '731 mi', 'Denali': '4,621 mi',
                   'Williamson': '5.44 mi', 'Shasta': '335 mi'}
