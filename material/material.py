class Material:

    def __init__(self, name, elastic_modulus, poisson, thermal_expansion, initial_yield):
        if elastic_modulus <= 0:
            raise ValueError(f"Elastic modulus {elastic_modulus} is not possible!")

        self._name = name
        self._elastic_modulus = elastic_modulus
        self._poisson = poisson
        self._thermal_expansion = thermal_expansion
        self._initial_yield = initial_yield

    @property
    def name(self):
        return self._name
    
    @property
    def elastic_modulus(self):
        return self._elastic_modulus

    @property
    def poisson(self):
        return self._poisson

    @property
    def thermal_expansion(self):
        return self._thermal_expansion

    @property
    def initial_yield(self):
        return self._initial_yield

    def __repr__(self):
        return (
            f"{typename(self)}"
            f"(name={self.name}, "
            f"elastic_modulus={self.elastic_modulus}, "
            f"poisson={self.poisson}, "
            f"thermal_expansion={self.thermal_expansion}, "
            f"initial_yield={self.initial_yield})"
        )

    def __str__(self):
        return (
            f"Material Name: {self.name}\n"
            f"Elastic Modulus: {self.elastic_modulus}\n"
            f"Poisson's Ratio: {self.poisson}\n"
            f"Coefficient of Thermal Expansion: {self.thermal_expansion}\n"
            f"Initial Yield Strength: {self.initial_yield}\n"
        )

def typename(obj):
    return type(obj).__name__
