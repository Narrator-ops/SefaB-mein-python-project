class Pokemon:

    def __init__(self, name, leben, skills: list[Skill], element):
        self.name = name
        self.leben = leben
        self.skills = skills
        self.element = element

    def use_skill(self, skill_nr, ziel : Pokemon):
        # [Skill1, Skill2, ...]
        self.skills[skill_nr].use(ziel)


