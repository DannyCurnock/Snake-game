from turtle import Turtle
SARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
LEFT = 180
DOWN = 270
UP = 90


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
   
   
    def create_snake(self):
        for position in SARTING_POSITIONS:
            self.add_segment(position)
            

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.goto(position)
        new_segment.color("white")
        self.segments.append(new_segment)


    def extend(self):
        self.add_segment(self.segments[-1].position())
        

    def move(self):
        # Len of the sqaures = 3, -1 because we need the sqaure at index position 2
        # because that is the last seg in the list, then stop at index 0 and step backwards throgh the list
        for sqaure_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[sqaure_num -1].xcor()
            new_y = self.segments[sqaure_num -1].ycor()
            self.segments[sqaure_num].goto(new_x, new_y) # Last segement(sqaure)
            # Goes to the second to last segment and the second to last to first
        self.head.fd(MOVE_DISTANCE)# Gets the segemnt in the f

   
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)    


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)   


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
