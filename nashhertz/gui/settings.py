import enum


class FilterImplementation(enum.Enum):
	LUMPED = 1
	DISTRIBUTED = 2
	ACTIVE = 3
	SWITCHED_CAPACITOR = 4	
	DIGITAL = 5
	
IMPLEMENTATION_DESCRIPTION = {
    FilterImplementation.LUMPED : "Lumped Synthesis",
    FilterImplementation.DISTRIBUTED : "Distributed Synthesis",
    FilterImplementation.ACTIVE : "Active Synthesis",
    FilterImplementation.SWITCHED_CAPACITOR : "Switched Capacitor Synthesis",
    FilterImplementation.DIGITAL : "Digital Synthesis"
}

TOPOLOGY_OPTIONS = {
    "Bessel" : {
        "Lumped Synthesis": {
            "Low Pass": [
                "Minimum Inductors",
                "Minimum Capacitors",
                "Singly Terminated at Load",
                "Singly Terminated at Source"
            ],
            "High Pass": [
                "Minimum Inductors",
                "Minimum Capacitors",
                "Singly Terminated at Load",
                "Singly Terminated at Source"
            ],
            "Band Pass": [
                "Classical",
                "Equal Inductors",
                "Equal Shunt Legs",
                "High/Low Pass",
                "Coupled Resonator Series C",
                "Coupled Resonator Shunt C",
                "Tubular",
                "Inductor Coupled",
                "Singly Terminated at Load",
                "Singly Terminated at Source"
            ],
            "Band Stop": [
                "Classical",
                "Singly Terminated at Load",
                "Singly Terminated at Source"
            ]
        },
        "Distributed Synthesis": {
            "Low Pass": [
                "Minimum Segments",
                "Minimum Stubs",
                "Split Stubs",
                "Stepped Impedance",
                "Spaced Stubs",
                "Radial Stubs",
                "Butterfly Stubs"
            ],
            "High Pass": [
                "Minimum Capacitors",
                "Minimum Stubs",
                "Minimum Segments",
                "Coupled Segments",
                "Spaced Stubs"
            ],
            "Band Pass": [
                "Minimum Segments",
                "Minimum Stubs",
                "Stepped Impedance",
                "Shunt Stub Resonators",
                "Open Stub Resonators",
                "Parallel Edge Tapped",
                "Parallel Edge Untapped",
                "Parallel Edge Equal Width",
                "Hairpin Resonators",
                "Miniature Hairpin Resonators",
                "Ring Resonators",
                "Interdigital",
                "Interdigital, Narrow Band",
                "Combline"
            ],
            "Band Stop": [
                "Stepped Stub Resonators",
                "Single Stub Resonator",
                "Notch Resonators, Open",
                "Not Resonators, Vias",
                "Spaced Stubs"
            ]
        },
        "Active Synthesis": {
            "Low Pass": [
                "Thomas 1",
                "Thomas 2",
                "Akerberg",
                "Sallen & Key",
                "MFB",
                "Leap Frog",
                "Parallel",
                "GIC Biquad",
                "GIC Ladder"
            ],
            "High Pass": [
                "Thomas 1",
                "Thomas 2",
                "Akerberg",
                "Sallen & Key",
                "MFB",
                "Leap Frog",
                "Parallel",
                "GIC Biquad",
                "GIC Ladder"
            ],
            "Band Pass": [
                "Thomas 1",
                "Thomas 2",
                "Akerberg",
                "Sallen & Key",
                "Twin T",
                "MFB",
                "Leap Frog",
                "Parallel",
                "GIC Biquad",
                "GIC Ladder"
            ],
            "Band Stop": [
                "Thomas 1",
                "Thomas 2",
                "Akerberg",
                "Sallen & Key",
                "Twin T",
                "MFB",
                 "Parallel",
                "GIC Biquad"
            ]
        },
        "Switched Capacitor Synthesis": {
            "Low Pass": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified"
            ],
            "High Pass": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified"
            ],
            "Band Pass": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified"
            ],
            "Band Stop": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified"
            ]
        },
        "Digital Synthesis": {
            "Low Pass": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified",
                "FIR Approximation"
            ],
            "High Pass": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified",
                "FIR Approximation"
            ],
            "Band Pass": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified",
                "FIR Approximation"
            ],
            "Band Stop": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified",
                "FIR Approximation"
            ]
        }
    } # Bessel
    "Butterworth" : {
        "Lumped Synthesis": {
            "Low Pass": [
                "Minimum Inductors",
                "Minimum Capacitors",
                "Singly Terminated at Load",
                "Singly Terminated at Source"
            ],
            "High Pass": [
                "Minimum Inductors",
                "Minimum Capacitors",
                "Singly Terminated at Load",
                "Singly Terminated at Source"
            ],
            "Band Pass": [
                "Classical",
                "Equal Inductors",
                "Equal Shunt Legs",
                "High/Low Pass",
                "Coupled Resonator Series C",
                "Coupled Resonator Shunt C",
                "Tubular",
                "Inductor Coupled",
                "Singly Terminated at Load",
                "Singly Terminated at Source"
            ],
            "Band Stop": [
                "Classical",
                "Singly Terminated at Load",
                "Singly Terminated at Source"
            ]
        },
        "Distributed Synthesis": {
            "Low Pass": [
                "Minimum Segments",
                "Minimum Stubs",
                "Split Stubs",
                "Stepped Impedance",
                "Spaced Stubs",
                "Radial Stubs",
                "Butterfly Stubs"
            ],
            "High Pass": [
                "Minimum Capacitors",
                "Minimum Stubs",
                "Minimum Segments",
                "Coupled Segments",
                "Spaced Stubs"
            ],
            "Band Pass": [
                "Minimum Segments",
                "Minimum Stubs",
                "Stepped Impedance",
                "Shunt Stub Resonators",
                "Open Stub Resonators",
                "Parallel Edge Tapped",
                "Parallel Edge Untapped",
                "Parallel Edge Equal Width",
                "Hairpin Resonators",
                "Miniature Hairpin Resonators",
                "Ring Resonators",
                "Interdigital",
                "Interdigital, Narrow Band",
                "Combline"
            ],
            "Band Stop": [
                "Stepped Stub Resonators",
                "Single Stub Resonator",
                "Notch Resonators, Open",
                "Not Resonators, Vias",
                "Spaced Stubs"
            ]
        },
        "Active Synthesis": {
            "Low Pass": [
                "Thomas 1",
                "Thomas 2",
                "Akerberg",
                "Sallen & Key",
                "MFB",
                "Leap Frog",
                "Parallel",
                "GIC Biquad",
                "GIC Ladder"
            ],
            "High Pass": [
                "Thomas 1",
                "Thomas 2",
                "Akerberg",
                "Sallen & Key",
                "MFB",
                "Leap Frog",
                "Parallel",
                "GIC Biquad",
                "GIC Ladder"
            ],
            "Band Pass": [
                "Thomas 1",
                "Thomas 2",
                "Akerberg",
                "Sallen & Key",
                "Twin T",
                "MFB",
                "Leap Frog",
                "Parallel",
                "GIC Biquad",
                "GIC Ladder"
            ],
            "Band Stop": [
                "Thomas 1",
                "Thomas 2",
                "Akerberg",
                "Sallen & Key",
                "Twin T",
                "MFB",
                 "Parallel",
                "GIC Biquad"
            ]
        },
        "Switched Capacitor Synthesis": {
            "Low Pass": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified"
            ],
            "High Pass": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified"
            ],
            "Band Pass": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified"
            ],
            "Band Stop": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified"
            ]
        },
        "Digital Synthesis": {
            "Low Pass": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified",
                "FIR Approximation"
            ],
            "High Pass": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified",
                "FIR Approximation"
            ],
            "Band Pass": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified",
                "FIR Approximation"
            ],
            "Band Stop": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified",
                "FIR Approximation"
            ]
        }
    } # Butterworth
    "Chebyshev I" : {
        "Lumped Synthesis": {
            "Low Pass": [
                "Minimum Inductors",
                "Minimum Capacitors",
                "Singly Terminated at Load",
                "Singly Terminated at Source"
            ],
            "High Pass": [
                "Minimum Inductors",
                "Minimum Capacitors",
                "Singly Terminated at Load",
                "Singly Terminated at Source"
            ],
            "Band Pass": [
                "Classical",
                "Equal Inductors",
                "Equal Shunt Legs",
                "High/Low Pass",
                "Coupled Resonator Series C",
                "Coupled Resonator Shunt C",
                "Tubular",
                "Inductor Coupled",
                "Singly Terminated at Load",
                "Singly Terminated at Source"
            ],
            "Band Stop": [
                "Classical",
                "Singly Terminated at Load",
                "Singly Terminated at Source"
            ]
        },
        "Distributed Synthesis": {
            "Low Pass": [
                "Minimum Segments",
                "Minimum Stubs",
                "Split Stubs",
                "Stepped Impedance",
                "Spaced Stubs",
                "Radial Stubs",
                "Butterfly Stubs"
            ],
            "High Pass": [
                "Minimum Capacitors",
                "Minimum Stubs",
                "Minimum Segments",
                "Coupled Segments",
                "Spaced Stubs"
            ],
            "Band Pass": [
                "Minimum Segments",
                "Minimum Stubs",
                "Stepped Impedance",
                "Shunt Stub Resonators",
                "Open Stub Resonators",
                "Parallel Edge Tapped",
                "Parallel Edge Untapped",
                "Parallel Edge Equal Width",
                "Hairpin Resonators",
                "Miniature Hairpin Resonators",
                "Ring Resonators",
                "Interdigital",
                "Interdigital, Narrow Band",
                "Combline"
            ],
            "Band Stop": [
                "Stepped Stub Resonators",
                "Single Stub Resonator",
                "Notch Resonators, Open",
                "Not Resonators, Vias",
                "Spaced Stubs"
            ]
        },
        "Active Synthesis": {
            "Low Pass": [
                "Thomas 1",
                "Thomas 2",
                "Akerberg",
                "Sallen & Key",
                "MFB",
                "Leap Frog",
                "Parallel",
                "GIC Biquad",
                "GIC Ladder"
            ],
            "High Pass": [
                "Thomas 1",
                "Thomas 2",
                "Akerberg",
                "Sallen & Key",
                "MFB",
                "Leap Frog",
                "Parallel",
                "GIC Biquad",
                "GIC Ladder"
            ],
            "Band Pass": [
                "Thomas 1",
                "Thomas 2",
                "Akerberg",
                "Sallen & Key",
                "Twin T",
                "MFB",
                "Leap Frog",
                "Parallel",
                "GIC Biquad",
                "GIC Ladder"
            ],
            "Band Stop": [
                "Thomas 1",
                "Thomas 2",
                "Akerberg",
                "Sallen & Key",
                "Twin T",
                "MFB",
                 "Parallel",
                "GIC Biquad"
            ]
        },
        "Switched Capacitor Synthesis": {
            "Low Pass": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified"
            ],
            "High Pass": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified"
            ],
            "Band Pass": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified"
            ],
            "Band Stop": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified"
            ]
        },
        "Digital Synthesis": {
            "Low Pass": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified",
                "FIR Approximation"
            ],
            "High Pass": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified",
                "FIR Approximation"
            ],
            "Band Pass": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified",
                "FIR Approximation"
            ],
            "Band Stop": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified",
                "FIR Approximation"
            ]
        }
    } # Chebyshev I
    "Chebyshev II" : {
        "Lumped Synthesis": {
            "Low Pass": [
                "Minimum Inductors",
                "Minimum Capacitors",
                "Singly Terminated at Load",
                "Singly Terminated at Source"
            ],
            "High Pass": [
                "Minimum Inductors",
                "Minimum Capacitors",
                "Singly Terminated at Load",
                "Singly Terminated at Source"
            ],
            "Band Pass": [
                "Classical",
                "Equal Inductors",
                "Equal Shunt Legs",
                "High/Low Pass",
                "Coupled Resonator Series C",
                "Coupled Resonator Shunt C",
                "Tubular",
                "Inductor Coupled",
                "Singly Terminated at Load",
                "Singly Terminated at Source"
            ],
            "Band Stop": [
                "Classical",
                "Singly Terminated at Load",
                "Singly Terminated at Source"
            ]
        },
        "Distributed Synthesis": {
            "Low Pass": [
                "Minimum Segments",
                "Minimum Stubs",
                "Split Stubs",
                "Stepped Impedance",
                "Spaced Stubs",
                "Radial Stubs",
                "Butterfly Stubs"
            ],
            "High Pass": [
                "Minimum Capacitors",
                "Minimum Stubs",
                "Minimum Segments",
                "Coupled Segments",
                "Spaced Stubs"
            ],
            "Band Pass": [
                "Minimum Segments",
                "Minimum Stubs",
                "Stepped Impedance",
                "Shunt Stub Resonators",
                "Open Stub Resonators",
                "Parallel Edge Tapped",
                "Parallel Edge Untapped",
                "Parallel Edge Equal Width",
                "Hairpin Resonators",
                "Miniature Hairpin Resonators",
                "Ring Resonators",
                "Interdigital",
                "Interdigital, Narrow Band",
                "Combline"
            ],
            "Band Stop": [
                "Stepped Stub Resonators",
                "Single Stub Resonator",
                "Notch Resonators, Open",
                "Not Resonators, Vias",
                "Spaced Stubs"
            ]
        },
        "Active Synthesis": {
            "Low Pass": [
                "Thomas 1",
                "Thomas 2",
                "Akerberg",
                "Sallen & Key",
                "MFB",
                "Leap Frog",
                "Parallel",
                "GIC Biquad",
                "GIC Ladder"
            ],
            "High Pass": [
                "Thomas 1",
                "Thomas 2",
                "Akerberg",
                "Sallen & Key",
                "MFB",
                "Leap Frog",
                "Parallel",
                "GIC Biquad",
                "GIC Ladder"
            ],
            "Band Pass": [
                "Thomas 1",
                "Thomas 2",
                "Akerberg",
                "Sallen & Key",
                "Twin T",
                "MFB",
                "Leap Frog",
                "Parallel",
                "GIC Biquad",
                "GIC Ladder"
            ],
            "Band Stop": [
                "Thomas 1",
                "Thomas 2",
                "Akerberg",
                "Sallen & Key",
                "Twin T",
                "MFB",
                 "Parallel",
                "GIC Biquad"
            ]
        },
        "Switched Capacitor Synthesis": {
            "Low Pass": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified"
            ],
            "High Pass": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified"
            ],
            "Band Pass": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified"
            ],
            "Band Stop": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified"
            ]
        },
        "Digital Synthesis": {
            "Low Pass": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified",
                "FIR Approximation"
            ],
            "High Pass": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified",
                "FIR Approximation"
            ],
            "Band Pass": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified",
                "FIR Approximation"
            ],
            "Band Stop": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified",
                "FIR Approximation"
            ]
        }
    } # Chebyshev II
    "Elliptic" : {
        "Lumped Synthesis": {
            "Low Pass": [
                "Minimum Inductors",
                "Minimum Capacitors",
                "Singly Terminated at Load",
                "Singly Terminated at Source"
            ],
            "High Pass": [
                "Minimum Inductors",
                "Minimum Capacitors",
                "Singly Terminated at Load",
                "Singly Terminated at Source"
            ],
            "Band Pass": [
                "Classical",
                "Equal Inductors",
                "Equal Shunt Legs",
                "High/Low Pass",
                "Coupled Resonator Series C",
                "Coupled Resonator Shunt C",
                "Tubular",
                "Inductor Coupled",
                "Singly Terminated at Load",
                "Singly Terminated at Source"
            ],
            "Band Stop": [
                "Classical",
                "Singly Terminated at Load",
                "Singly Terminated at Source"
            ]
        },
        "Distributed Synthesis": {
            "Low Pass": [
                "Minimum Segments",
                "Minimum Stubs",
                "Split Stubs",
                "Stepped Impedance",
                "Spaced Stubs",
                "Radial Stubs",
                "Butterfly Stubs"
            ],
            "High Pass": [
                "Minimum Capacitors",
                "Minimum Stubs",
                "Minimum Segments",
                "Coupled Segments",
                "Spaced Stubs"
            ],
            "Band Pass": [
                "Minimum Segments",
                "Minimum Stubs",
                "Stepped Impedance",
                "Shunt Stub Resonators",
                "Open Stub Resonators",
                "Parallel Edge Tapped",
                "Parallel Edge Untapped",
                "Parallel Edge Equal Width",
                "Hairpin Resonators",
                "Miniature Hairpin Resonators",
                "Ring Resonators",
                "Interdigital",
                "Interdigital, Narrow Band",
                "Combline"
            ],
            "Band Stop": [
                "Stepped Stub Resonators",
                "Single Stub Resonator",
                "Notch Resonators, Open",
                "Not Resonators, Vias",
                "Spaced Stubs"
            ]
        },
        "Active Synthesis": {
            "Low Pass": [
                "Thomas 1",
                "Thomas 2",
                "Akerberg",
                "Sallen & Key",
                "MFB",
                "Leap Frog",
                "Parallel",
                "GIC Biquad",
                "GIC Ladder"
            ],
            "High Pass": [
                "Thomas 1",
                "Thomas 2",
                "Akerberg",
                "Sallen & Key",
                "MFB",
                "Leap Frog",
                "Parallel",
                "GIC Biquad",
                "GIC Ladder"
            ],
            "Band Pass": [
                "Thomas 1",
                "Thomas 2",
                "Akerberg",
                "Sallen & Key",
                "Twin T",
                "MFB",
                "Leap Frog",
                "Parallel",
                "GIC Biquad",
                "GIC Ladder"
            ],
            "Band Stop": [
                "Thomas 1",
                "Thomas 2",
                "Akerberg",
                "Sallen & Key",
                "Twin T",
                "MFB",
                 "Parallel",
                "GIC Biquad"
            ]
        },
        "Switched Capacitor Synthesis": {
            "Low Pass": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified"
            ],
            "High Pass": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified"
            ],
            "Band Pass": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified"
            ],
            "Band Stop": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified"
            ]
        },
        "Digital Synthesis": {
            "Low Pass": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified",
                "FIR Approximation"
            ],
            "High Pass": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified",
                "FIR Approximation"
            ],
            "Band Pass": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified",
                "FIR Approximation"
            ],
            "Band Stop": [
                "Bilinear",
                "Matched Z",
                "Impulse Invariant",
                "Step Invariant",
                "Impulse Invariant, Modified",
                "Step Invariant, Modified",
                "FIR Approximation"
            ]
        }
    } # Elliptic
}
        
