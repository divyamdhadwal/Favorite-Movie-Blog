import media  # Contains the class and functions to show movie related info
import fresh_tomatoes  # This file generates HTML page for given python code

# Creating several instances of class movie & passing information into them.
the_revenant = media.Movie("The Revenant", "A movie about the survival skills",
                           "https://goo.gl/K5XfUu",
                           "https://youtu.be/LoebZZ8K5N0")
skyfall = media.Movie("James Bond Skyfall",
                      "A movie featuring a British agent",
                      "https://goo.gl/PcfcNM",
                      "https://youtu.be/6kw1UVovByw")
spectre = media.Movie("James Bond Spectre",
                      "A movie featuring a British agent",
                      "https://goo.gl/Mcxsrz",
                      "https://youtu.be/7GqClqvlObY")
mi_ghostprotocol = media.Movie("Mision Impossible Ghost Protocol",
                               "A movie about US Secret agent.",
                               "https://goo.gl/apkLTR",
                               "https://youtu.be/hR-0po0hzDQ")
fourth_kind = media.Movie("The Fourth Kind",
                          "A movie based on Alien abductions in Alaska",
                          "https://goo.gl/hmKuNa",
                          "https://youtu.be/r25ZUxTURis")
nfs = media.Movie("Need for Speed 2014",
                  "A street racer is framed by a rival.",
                  "https://goo.gl/41hD11",
                  "https://youtu.be/u3wtVI-aJuw")

# Datastructure to store my favourite movies.
movie = [the_revenant, skyfall, spectre, mi_ghostprotocol, fourth_kind, nfs]

# Call open_movies_page function located inside fresh tomatoes file.
fresh_tomatoes.open_movies_page(movie)

