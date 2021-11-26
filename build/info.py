selected_peaks = []

peaks_title = {'Whitney': 'Mt. Whitney', 'Elbert': 'Mt. Elbert', 'Rainier': 'Mt. Rainier', 'Denali': 'Denali'
    , 'Williamson': 'Mt. Williamson', 'Shasta': 'Mt. Shasta'}

peaks_url = {'Whitney': 'Mount_Whitney', 'Elbert': 'Mount_Elbert', 'Rainier': 'Mount_Rainier', 'Denali': 'Denali'
    , 'Williamson': "Mount_Williamson", 'Shasta': 'Mount_Shasta'}

peaks_dict = {"Whitney": 'The most popular route to the summit is by way of the Mount Whitney Trail, which starts at '
                         'Whitney Portal, at an elevation of 8,360 ft (2,548 m), 13 mi (21 km) west of the town of '
                         'Lone Pine. The hike is about 22 mi (35 km) round trip with an elevation gain of over 6'
                         '100 ft (1,859 m)',
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
