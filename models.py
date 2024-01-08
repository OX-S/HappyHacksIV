class School:
    def __init__(self, school_id, name, latitude, longitude, donation_goal, current_funds, description, school_img):
        self.id = school_id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.donation_goal = donation_goal
        self.current_funds = current_funds
        self.description = description
        self.school_img = school_img
