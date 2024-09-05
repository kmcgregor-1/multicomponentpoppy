import numpy as np
from fitburst.analysis.model import SpectrumModeler
import matplotlib.pyplot as plt
import json

with open("./examples/sample_pop", 'r') as sample_pop:
    multicomponent_pop = json.load(sample_pop)

freqs = np.linspace(400.,800.,1024) # array of frequency labels, in MHz
times = np.arange(0,100,0.983) # array of timestamps, in milliseconds

# define dictiomary containing parameter values.

burst_parameters = {                                                     
    "amplitude"            : [1.5,1.], 
    "arrival_time"         : [40.,50.],
    "burst_width"          : [1.,0.5],
    "dm"                   : [349.5,349.5], 
    "dm_index"             : [-2.,-2.],
    "ref_freq"             : [600.,650.],
    "scattering_index"     : [-2.,-2.],
    "scattering_timescale" : [0.,0.],
    "spectral_index"       : [10.,10.],
    "spectral_running"     : [-100.,-100.],
}

# now instantiate the SpectrumModeler for a three-component model.
def generate_spectrum(bps):
    del bps["num_components"]
    num_components = len(bps["dm"])
    model = SpectrumModeler(freqs, times, num_components = num_components)

    # now update Gaussian-SED model object to use the above values.
    model.update_parameters(bps)

    # grab the model spectrum.
    spectrum_model = model.compute_model()
    return spectrum_model

burst_num = 0
for event in multicomponent_pop[:5]:

    fig, ax = plt.subplots()

    ax.imshow(generate_spectrum(event), extent=[0,100, 400, 800],aspect='auto')

    ax.set_xlabel("Time (ms)")
    ax.set_ylabel("Frequency (MHz)")

    plt.tight_layout()
    plt.savefig("./model_spectra/model_burst_"+str(burst_num)+".png")
    burst_num += 1


