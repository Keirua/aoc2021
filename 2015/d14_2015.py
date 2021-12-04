import aoc
import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

input = aoc.input_as_string(aoc.challenge_filename(14, 2015))

test_input= """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""


from dataclasses import dataclass
import enum

class State(enum.Enum):
    TRAVELLING = "travelling"
    RESTING = "resting"
@dataclass
class Reindeer:
    name: str
    speed: int
    speed_capacity: int
    rest_duration: int

    def compute2(self, duration):
        # total_distance =
        nb_full_movements = duration // (self.speed_capacity + self.rest_duration)
        nb_partial_movements = duration % (self.speed_capacity + self.rest_duration)
        if nb_partial_movements > self.speed_capacity:
            nb_partial_movements = self.speed_capacity
        # else:
        #     nb_partial_movements =

        return (nb_partial_movements + nb_full_movements*self.speed_capacity) * self.speed


    # def compute_distance_travelled(self, duration):
    #     t=0
    #     distance_travelled = 0
    #     state = State.TRAVELLING
    #     cooldown = self.speed_capacity
    #     while t < duration:
    #         if state == State.TRAVELLING:
    #             distance_travelled += self.speed
    #             cooldown -= 1
    #             if cooldown == 0:
    #                 state = State.RESTING
    #                 cooldown = self.rest_duration
    #         if state == State.RESTING:
    #             cooldown -= 1
    #             if cooldown == 0:
    #                 state = State.TRAVELLING
    #                 cooldown = self.speed_capacity
    #         t += 1
    #     return distance_travelled



def parse(input):
    input = re.findall(r"(.*) can fly (.*) km/s for (.*) seconds, but then must rest for (.*) seconds.", input)
    return [Reindeer(name, int(s), int(c), int(d)) for name, s, c, d in input]

reinders = parse(input)
# reinders = parse(test_input)

# print(input)
# pp.pprint(reinders)
max_distance = 0
for r in reinders:
    d = r.compute2(2503)
    # d = r.compute_distance_travelled(2503)
    if d > max_distance:
        max_distance = d
    print(r.name, d)

print(max_distance)
