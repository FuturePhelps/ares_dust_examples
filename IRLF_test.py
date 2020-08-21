import ares
import matplotlib.pyplot as plt

# Create a GalaxyEnsemble object from the parameters
pars = ares.util.ParameterBundle('mirocha2020:univ')
pop = ares.populations.GalaxyPopulation(**pars)

# Generate a stellar luminosity function at lambda = 1600 angstroms
x1, phi1 = pop.LuminosityFunction(6, None, wave = 1600)

# Generate a dust IR luminosty function at lambda = 3e5 angstroms
x2, phi2 = pop.LuminosityFunction(6, None, wave = 3e5)

# Both LFs are in absolute magnitudes since mags = True by default

# Plot and save as pdf and png in the figures folder
fig, ax = plt.subplots(1,1)
fig.set_size_inches(6.5, 3.7)
ax.semilogy(x1, phi1, label = r'stellar luminosity (1600 $\AA$)')
ax.semilogy(x2, phi2, label = r'dust luminosity (300 000 $\AA$)')
ax.legend()
ax.set_title(r"Galaxy Luminosity Functions")
ax.set_xlabel(r"Absolute Magnitude")
ax.set_ylabel(r"$\phi$ [$\mathrm{mag}^{-1}\mathrm{c}\mathrm{Mpc}^{-3}$]")
fig.savefig("figures/IRLF.pdf", bbox_inches = 'tight')
fig.savefig("figures/IRLF.png", bbox_inches = 'tight')