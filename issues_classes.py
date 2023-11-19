from pydantic import BaseModel


class BookModel(BaseModel):
    title: str
    author: str
    year: int

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class Magazine(BookModel):
    def __str__(self):
        return (
            f"Title: {self.title}, Magazine Author: {self.author},"
            + f"Year: {self.year}"
        )
