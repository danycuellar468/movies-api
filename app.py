from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Movies API")

class Movie(BaseModel):
    name: str
    imageName: str
    description: str

SEED: List[Movie] = [
    Movie(name="Freaky Friday", imageName="FreakyFriday",
          description="An overworked mother and her daughter do not get along. When they switch bodies, each is forced to adapt to the other's life for one freaky Friday."),
    Movie(name="Lemonade Mouth", imageName="LemonadeMouth",
          description="Five high school kids, Olivia, Wendall, Stella, Charlie, and Mo, meet in detention and start a band based on the lemonade vending machine outside the detention room."),
    Movie(name="Twitches", imageName="Twitches",
          description="Twin witches who were separated at birth and were adopted by two different families meet on their 21st birthday and must use their powers to save the world in which they were born, where their birth mother still lives."),
    Movie(name="Princess Protection Program", imageName="PPP",
          description="A princess whose country has been invaded goes into hiding in Louisiana, where she has to learn to act like an ordinary teenager."),
    Movie(name="Camp Rock", imageName="CampRock",
          description="At a music camp for gifted teens, a popular teen idol overhears a girl singing and sets out to find who the talented voice belongs to. What he doesn't know is that the girl is actually a camp kitchen worker with a fear of being heard."),
    Movie(name="Halloweentown", imageName="Halloweentown",
          description="When a young girl living with her secret witch mother learns she too is a witch, she must help her witch grandmother save Halloweentown from evil forces."),
    Movie(name="Hocus Pocus", imageName="HocusPocus",
          description="A teenage boy named Max and his little sister move to Salem, where he struggles to fit in before awakening a trio of diabolical witches that were executed in the 17th century."),
    Movie(name="Frenemies", imageName="Frenemies",
          description="Three sets of friends deal with the ups and downs of their ever-changing relationships."),
    Movie(name="Teen Beach Movie", imageName="TBM",
          description="Two surfing lovers, whose doomed relationship is nearing to a close, find themselves swept into a dimension-traversing wave that sends them into a beach movie musical in the 60's."),
    Movie(name="The Cheetah Girls", imageName="TCG",
          description="Four teens aim to take the world by storm with their music.")
]

@app.get("/movies", response_model=List[Movie])
def list_movies():
    return SEED