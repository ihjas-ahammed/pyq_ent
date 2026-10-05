import os
import subprocess

CSS = """
  @page {
    size: A4;
    margin: 20mm 15mm 20mm 15mm;
    @bottom-center {
      content: "Page " counter(page) " of " counter(pages);
      font-size: 9pt;
      color: #6b7280;
    }
  }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    color: #1f2937;
    line-height: 1.55;
    font-size: 10.5pt;
    margin: 0;
    padding: 0;
  }
  .header {
    text-align: center;
    border-bottom: 2.5px solid #1e3a8a;
    padding-bottom: 14px;
    margin-bottom: 20px;
  }
  .header .inst-logo-sub {
    font-size: 11pt;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: #4b5563;
    font-weight: 600;
    margin-bottom: 4px;
  }
  .header h1 {
    font-size: 21pt;
    color: #1e3a8a;
    margin: 0 0 6px 0;
    font-weight: 800;
    letter-spacing: -0.5px;
  }
  .header h2 {
    font-size: 14pt;
    color: #2563eb;
    margin: 0 0 8px 0;
    font-weight: 600;
  }
  .header .badge-bar {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-top: 8px;
  }
  .badge {
    background: #eff6ff;
    border: 1px solid #bfdbfe;
    color: #1d4ed8;
    padding: 3px 10px;
    border-radius: 9999px;
    font-size: 8.5pt;
    font-weight: 600;
  }
  .pattern-table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 24px;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    overflow: hidden;
  }
  .pattern-table th, .pattern-table td {
    padding: 9px 12px;
    border: 1px solid #cbd5e1;
    font-size: 9.5pt;
    text-align: left;
  }
  .pattern-table th {
    background: #1e3a8a;
    color: #ffffff;
    font-weight: 600;
  }
  .unit-card {
    border: 1px solid #e2e8f0;
    border-left: 4px solid #2563eb;
    border-radius: 0 6px 6px 0;
    padding: 12px 16px;
    margin-bottom: 14px;
    page-break-inside: avoid;
    background: #ffffff;
  }
  .unit-title {
    font-weight: 700;
    font-size: 11.5pt;
    color: #1e3a8a;
    margin-bottom: 6px;
  }
  .unit-topics {
    margin: 0;
    padding-left: 20px;
    color: #374151;
  }
  .unit-topics li {
    margin-bottom: 4px;
  }
  .topic-name {
    font-weight: 600;
    color: #111827;
  }
  .sec-heading {
    font-size: 14pt;
    font-weight: 700;
    color: #1e3a8a;
    border-bottom: 1.5px solid #cbd5e1;
    padding-bottom: 4px;
    margin-top: 24px;
    margin-bottom: 12px;
  }
"""

def generate_pdf(html_content, output_pdf):
    tmp_html = f"/tmp/cusat_syll_{os.path.basename(output_pdf)}.html"
    with open(tmp_html, "w", encoding="utf-8") as f:
        f.write(html_content)
    cmd = [
        'google-chrome-stable',
        '--headless=new',
        '--disable-gpu',
        '--no-pdf-header-footer',
        f'--print-to-pdf={output_pdf}',
        tmp_html
    ]
    subprocess.run(cmd, check=True)
    if os.path.exists(output_pdf) and os.path.getsize(output_pdf) > 1000:
        print(f"[GENERATED] {output_pdf} ({os.path.getsize(output_pdf)} bytes)")
    else:
        print(f"[FAILED] {output_pdf}")

# 1. CUSAT CAT UG Physics Syllabus
def get_cusat_ug_ph_html(year_str):
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>CUSAT CAT {year_str} - Physics Official Detailed Syllabus</title>
<style>{CSS}</style>
</head>
<body>
  <div class="header">
    <div class="inst-logo-sub">Cochin University of Science and Technology (CUSAT)</div>
    <h1>Common Admission Test (CAT {year_str})</h1>
    <h2>Official Detailed Syllabus & Blueprint: Physics (Test Code 101)</h2>
    <div class="badge-bar">
      <span class="badge">Curriculum: NCERT Class XI & XII Standard</span>
      <span class="badge">Level: Undergraduate & 5-Year Integrated M.Sc</span>
      <span class="badge">Session: {year_str}</span>
    </div>
  </div>

  <table class="pattern-table">
    <tr>
      <th>Parameter</th>
      <th>Examination Specification</th>
    </tr>
    <tr>
      <td><strong>Examination Mode</strong></td>
      <td>Computer Based Test (CBT) Online Examination</td>
    </tr>
    <tr>
      <td><strong>Total Questions (Physics Section)</strong></td>
      <td>75 Multiple Choice Questions (MCQs)</td>
    </tr>
    <tr>
      <td><strong>Marking Scheme</strong></td>
      <td>+3 marks for each correct response; -1 mark for each incorrect response (Negative marking applies)</td>
    </tr>
    <tr>
      <td><strong>Maximum Marks (Physics)</strong></td>
      <td>225 Marks</td>
    </tr>
    <tr>
      <td><strong>Eligible Programs</strong></td>
      <td>B.Tech, 5-Year Integrated M.Sc in Physics, Chemistry, Mathematics, Statistics, Marine Biology</td>
    </tr>
  </table>

  <div class="sec-heading">Class XI Syllabus Modules</div>

  <div class="unit-card">
    <div class="unit-title">Unit 1: Physics and Measurement</div>
    <ul class="unit-topics">
      <li><span class="topic-name">Scope & Dimensions:</span> Units of measurements, System of Units (SI Units), fundamental and derived units. Dimensions of physical quantities, dimensional analysis and its applications. Least count, significant figures, errors in measurement and combination of errors.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">Unit 2: Kinematics</div>
    <ul class="unit-topics">
      <li><span class="topic-name">Motion in 1D & 2D:</span> Frame of reference, Motion in a straight line: Position-time graph, speed and velocity. Uniform and non-uniform motion, average speed and instantaneous velocity, uniformly accelerated motion, velocity-time and position-time graphs, kinematic equations for acceleration. Scalars and vectors, vector addition, resolution, dot product and cross product. Unit vectors. Projectile motion and uniform circular motion.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">Unit 3: Laws of Motion</div>
    <ul class="unit-topics">
      <li><span class="topic-name">Dynamics:</span> Force and inertia, Newton's first, second, and third laws of motion. Momentum, impulse and law of conservation of linear momentum with applications. Equilibrium of concurrent forces. Static and kinetic friction, laws of friction, rolling friction, lubrication. Dynamics of uniform circular motion: Centripetal force, banking of roads.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">Unit 4: Work, Energy and Power</div>
    <ul class="unit-topics">
      <li><span class="topic-name">Energy & Collisions:</span> Work done by a constant force and variable force; Kinetic energy and work-energy theorem. Power. Potential energy of a spring, conservative and non-conservative forces, conservation of mechanical energy. Elastic and inelastic collisions in one and two dimensions.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">Unit 5: Rotational Motion & System of Particles</div>
    <ul class="unit-topics">
      <li><span class="topic-name">Rigid Body Dynamics:</span> Centre of mass of a two-particle system, momentum conservation and centre of mass motion. Torque, angular momentum and its conservation with applications. Moment of inertia, radius of gyration, parallel and perpendicular axes theorems. Moments of inertia of simple geometrical bodies. Equilibrium of rigid bodies.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">Unit 6: Gravitation</div>
    <ul class="unit-topics">
      <li><span class="topic-name">Planetary Motion & Fields:</span> Universal law of gravitation. Acceleration due to gravity and its variation with altitude and depth. Kepler's laws of planetary motion. Gravitational potential energy and gravitational potential. Escape speed, orbital velocity of satellites, geostationary satellites.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">Unit 7: Properties of Bulk Matter & Fluids</div>
    <ul class="unit-topics">
      <li><span class="topic-name">Elasticity & Hydrodynamics:</span> Hooke's law, stress-strain relationship, Young's modulus, bulk modulus, modulus of rigidity. Pascal's law and its applications (hydraulic lift). Viscosity, Stokes' law, terminal velocity, streamline and turbulent flow, critical velocity, Reynolds number. Bernoulli's principle. Surface energy, surface tension, angle of contact, excess pressure, capillary rise.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">Unit 8: Thermodynamics & Kinetic Theory of Gases</div>
    <ul class="unit-topics">
      <li><span class="topic-name">Thermal Physics:</span> Thermal equilibrium, zeroth, first and second laws of thermodynamics. Isothermal, adiabatic, isobaric, and isochoric processes. Reversible and irreversible processes, Carnot engine and efficiency. Kinetic theory of gases: Assumptions, concept of pressure, kinetic energy and temperature, RMS speed, degrees of freedom, law of equipartition of energy, specific heats of gases, mean free path.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">Unit 9: Oscillations and Waves</div>
    <ul class="unit-topics">
      <li><span class="topic-name">SHM & Acoustics:</span> Periodic motion, period, frequency, simple harmonic motion (SHM) and its equation; Phase, oscillations of a spring and simple pendulum. Free, forced, and damped oscillations, resonance. Wave motion: Longitudinal and transverse waves, speed of wave motion, displacement relation for a progressive wave. Principle of superposition of waves, reflection of waves, standing waves in strings and organ pipes, fundamental mode and harmonics, beats, Doppler effect in sound.</li>
    </ul>
  </div>

  <div class="sec-heading">Class XII Syllabus Modules</div>

  <div class="unit-card">
    <div class="unit-title">Unit 10: Electrostatics</div>
    <ul class="unit-topics">
      <li><span class="topic-name">Charges & Fields:</span> Electric charges, Coulomb's law, superposition principle, continuous charge distribution. Electric field, electric field lines, electric dipole, torque on a dipole. Gauss's law and applications (wire, sheet, sphere). Electric potential, potential difference, equipotential surfaces, electrical potential energy. Conductors and insulators, dielectrics, capacitors and capacitance, combination of capacitors, energy stored in a capacitor.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">Unit 11: Current Electricity</div>
    <ul class="unit-topics">
      <li><span class="topic-name">DC Circuits:</span> Electric current, drift velocity, mobility, Ohm's law, V-I characteristics, electrical resistance, resistivity and conductivity. Temperature dependence of resistance. Internal resistance of a cell, terminal voltage, emf, cells in series and parallel. Kirchhoff's laws and applications: Wheatstone bridge, Metre bridge, Potentiometer (principle, comparison of emf, internal resistance).</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">Unit 12: Magnetic Effects of Current and Magnetism</div>
    <ul class="unit-topics">
      <li><span class="topic-name">Biot-Savart & Ampere Laws:</span> Biot-Savart law, magnetic field due to current loop and solenoid. Ampere's circuital law. Force on a moving charge in magnetic and electric fields (Lorentz force), cyclotron. Force on a current-carrying conductor in a uniform magnetic field. Force between two parallel currents, torque on current loop, moving coil galvanometer and conversion to ammeter/voltmeter. Magnetic dipole, bar magnet, Earth's magnetic field and magnetic elements. Para-, dia-, and ferromagnetic substances, hysteresis.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">Unit 13: Electromagnetic Induction & Alternating Currents</div>
    <ul class="unit-topics">
      <li><span class="topic-name">Faraday & AC Circuits:</span> Electromagnetic induction, Faraday's laws, induced EMF and current, Lenz's law, Eddy currents. Self and mutual inductance. Alternating currents, peak and RMS value of AC; reactance and impedance; LCR series circuit, resonance, power in AC circuits, wattless current. AC generator and transformer.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">Unit 14: Electromagnetic Waves</div>
    <ul class="unit-topics">
      <li><span class="topic-name">EM Spectrum:</span> Displacement current, characteristics of EM waves, transverse nature. Electromagnetic spectrum (radio, microwaves, infrared, visible, ultraviolet, X-rays, gamma rays), properties and applications.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">Unit 15: Optics (Ray & Wave Optics)</div>
    <ul class="unit-topics">
      <li><span class="topic-name">Ray Optics:</span> Reflection of light, spherical mirrors, mirror formula. Refraction, total internal reflection, optical fibres, refraction at spherical surfaces, thin lens formula, lens maker's formula, magnification, power of a lens, combination of thin lenses. Dispersion through a prism. Optical instruments: Microscopes and astronomical telescopes (refracting and reflecting).</li>
      <li><span class="topic-name">Wave Optics:</span> Wave front and Huygens' principle, reflection and refraction of plane wave. Interference, Young's double-slit experiment, fringe width. Diffraction due to a single slit, width of central maximum. Polarization, Brewster's law, uses of plane polarized light and Polaroid.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">Unit 16: Modern Physics & Electronic Devices</div>
    <ul class="unit-topics">
      <li><span class="topic-name">Quantum, Nuclear & Electronics:</span> Photoelectric effect, Hertz and Lenard observations, Einstein's photoelectric equation, de Broglie relation, Davisson-Germer experiment. Alpha-particle scattering, Rutherford model, Bohr model, energy levels, hydrogen spectrum. Composition and size of nucleus, atomic masses, mass-energy relation, mass defect, binding energy, nuclear fission and fusion. Energy bands in conductors, semiconductors and insulators; intrinsic and extrinsic semiconductors, p-n junction, forward and reverse bias, diode as rectifier, I-V characteristics of LED, photodiode, solar cell, Zener diode as voltage regulator. Logic gates (OR, AND, NOT, NAND, NOR).</li>
    </ul>
  </div>
</body>
</html>
"""

# 2. CUSAT CAT PG MSc Physics Syllabus
def get_cusat_pg_ph_html():
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>CUSAT CAT - Post-Graduate M.Sc Physics Official Syllabus</title>
<style>{CSS}</style>
</head>
<body>
  <div class="header">
    <div class="inst-logo-sub">Cochin University of Science and Technology (CUSAT)</div>
    <h1>Post-Graduate Common Admission Test (PG CAT)</h1>
    <h2>Official Detailed Syllabus: M.Sc Physics (Test Code 612)</h2>
    <div class="badge-bar">
      <span class="badge">Program: M.Sc in Physics</span>
      <span class="badge">Level: Post-Graduate Entrance Examination</span>
      <span class="badge">Eligibility: B.Sc Physics Degree with Mathematics</span>
    </div>
  </div>

  <table class="pattern-table">
    <tr>
      <th>Parameter</th>
      <th>Examination Specification</th>
    </tr>
    <tr>
      <td><strong>Total Questions</strong></td>
      <td>150 Objective Multiple Choice Questions</td>
    </tr>
    <tr>
      <td><strong>Duration</strong></td>
      <td>2 Hours (120 Minutes)</td>
    </tr>
    <tr>
      <td><strong>Marking Scheme</strong></td>
      <td>+3 marks for correct response; -1 mark for incorrect response</td>
    </tr>
    <tr>
      <td><strong>Core Focus</strong></td>
      <td>Undergraduate (B.Sc) Physics core curriculum with auxiliary Mathematics</td>
    </tr>
  </table>

  <div class="unit-card">
    <div class="unit-title">1. Mathematical Physics</div>
    <ul class="unit-topics">
      <li>Vector calculus: gradient, divergence, curl, line, surface, and volume integrals; Stokes, Gauss, and Green theorems.</li>
      <li>Linear vector spaces, matrices, Cayley-Hamilton theorem, eigenvalues and eigenvectors.</li>
      <li>Complex analysis: Cauchy-Riemann conditions, Cauchy's theorem and residue calculus.</li>
      <li>Differential equations: first and second-order linear ODEs, Frobenius method, Legendre, Hermite, and Bessel special functions.</li>
      <li>Fourier series, Fourier transforms, Laplace transforms, and basic probability theory.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">2. Classical Mechanics</div>
    <ul class="unit-topics">
      <li>Newtonian mechanics of single and multi-particle systems, conservation laws, centre of mass.</li>
      <li>Constraints, generalized coordinates, D'Alembert's principle, Lagrange's equations and applications.</li>
      <li>Central force problem, Kepler's laws of planetary motion, scattering in a central field.</li>
      <li>Rigid body dynamics: inertia tensor, Euler angles, Euler's equations of motion.</li>
      <li>Hamiltonian formulation: canonical equations of motion, Poisson brackets, small oscillations, normal modes.</li>
      <li>Special theory of relativity: Lorentz transformations, length contraction, time dilation, relativistic energy-momentum.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">3. Electromagnetic Theory & Electrodynamics</div>
    <ul class="unit-topics">
      <li>Electrostatics: Laplace and Poisson equations, boundary value problems, method of images, multipole expansion.</li>
      <li>Magnetostatics: Biot-Savart law, Ampere's circuital law, vector potential, magnetic dipole.</li>
      <li>Electrodynamics: Maxwell's equations in vacuum and matter, gauge transformations (Coulomb and Lorenz gauges), Poynting theorem.</li>
      <li>Propagation of EM waves in linear dielectric and conducting media, reflection, refraction, Fresnel formulas.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">4. Quantum Mechanics</div>
    <ul class="unit-topics">
      <li>Inadequacy of classical physics, wave-particle duality, uncertainty principle, wave packet.</li>
      <li>Schrödinger wave equation (time-dependent and time-independent), probability interpretation, operators and observables.</li>
      <li>One-dimensional potentials: infinite square well, finite square well, potential barrier, delta function potential, harmonic oscillator.</li>
      <li>Schrödinger equation in 3D: hydrogen atom, orbital angular momentum, spherical harmonics.</li>
      <li>Spin angular momentum, Pauli spin matrices, addition of angular momenta. Time-independent perturbation theory.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">5. Thermodynamics and Statistical Physics</div>
    <ul class="unit-topics">
      <li>Laws of thermodynamics, thermodynamic potentials, Maxwell's relations, phase transitions, Clausius-Clapeyron equation.</li>
      <li>Microstates and macrostates, phase space, ensemble theory (microcanonical, canonical, and grand canonical ensembles).</li>
      <li>Maxwell-Boltzmann statistics, equipartition theorem, ideal gas.</li>
      <li>Quantum statistics: Fermi-Dirac distribution, degenerate Fermi gas, Bose-Einstein distribution, Planck black-body radiation formula, Bose-Einstein condensation.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">6. Solid State & Condensed Matter Physics</div>
    <ul class="unit-topics">
      <li>Crystal structures, reciprocal lattice, X-ray diffraction, Bragg's law, Laue conditions.</li>
      <li>Lattice vibrations, phonons, specific heat (Einstein and Debye models).</li>
      <li>Free electron theory of metals, Drude-Lorentz model, electrical and thermal conductivity, Wiedemann-Franz law.</li>
      <li>Band theory of solids, Bloch's theorem, Kronig-Penney model, semiconductors, effective mass. Superconductivity: Meissner effect, Type I/II, BCS overview.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">7. Electronics and Atomic/Nuclear Physics</div>
    <ul class="unit-topics">
      <li>Semiconductor physics, p-n junctions, bipolar junction transistors (BJT), field effect transistors (FET), operational amplifiers (Op-Amps) and configurations.</li>
      <li>Digital electronics: Boolean algebra, logic gates, flip-flops, counters, registers.</li>
      <li>Atomic spectra: Bohr-Sommerfeld model, LS and jj coupling, Zeeman effect, Stark effect.</li>
      <li>Nuclear properties: binding energy, nuclear models (liquid drop, shell model), radioactive decay laws, nuclear reactions, elementary particles.</li>
    </ul>
  </div>
</body>
</html>
"""

# 3. CUSAT CAT UG Mathematics Syllabus
def get_cusat_ug_mt_html(year_str):
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>CUSAT CAT {year_str} - Mathematics Official Detailed Syllabus</title>
<style>{CSS}</style>
</head>
<body>
  <div class="header">
    <div class="inst-logo-sub">Cochin University of Science and Technology (CUSAT)</div>
    <h1>Common Admission Test (CAT {year_str})</h1>
    <h2>Official Detailed Syllabus & Blueprint: Mathematics (Test Code 101)</h2>
    <div class="badge-bar">
      <span class="badge">Curriculum: NCERT Class XI & XII Standard</span>
      <span class="badge">Level: Undergraduate & 5-Year Integrated M.Sc</span>
      <span class="badge">Session: {year_str}</span>
    </div>
  </div>

  <table class="pattern-table">
    <tr>
      <th>Parameter</th>
      <th>Examination Specification</th>
    </tr>
    <tr>
      <td><strong>Examination Mode</strong></td>
      <td>Computer Based Test (CBT) Online Examination</td>
    </tr>
    <tr>
      <td><strong>Total Questions (Mathematics Section)</strong></td>
      <td>90 Multiple Choice Questions (Highest single weightage in CUSAT CAT)</td>
    </tr>
    <tr>
      <td><strong>Marking Scheme</strong></td>
      <td>+3 marks for each correct response; -1 mark for each incorrect response</td>
    </tr>
    <tr>
      <td><strong>Maximum Marks (Mathematics)</strong></td>
      <td>270 Marks</td>
    </tr>
    <tr>
      <td><strong>Ranking Criteria</strong></td>
      <td>Mathematics score is the mandatory tie-breaker in CUSAT engineering/science ranks</td>
    </tr>
  </table>

  <div class="sec-heading">Class XI Syllabus Modules</div>

  <div class="unit-card">
    <div class="unit-title">Unit 1: Sets, Relations, and Functions</div>
    <ul class="unit-topics">
      <li><span class="topic-name">Set Theory:</span> Sets and their representations, empty set, finite and infinite sets, equal sets, subsets, power set, universal set. Venn diagrams, union and intersection of sets, difference of sets, complement of a set, properties of complement.</li>
      <li><span class="topic-name">Relations & Functions:</span> Ordered pairs, Cartesian product of sets, number of elements in the Cartesian product. Definition of relation, domain, codomain and range of a relation. Functions as special relations, domain, codomain, range of real functions, constant, polynomial, rational, modulus, signum, exponential, logarithmic, and greatest integer functions.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">Unit 2: Complex Numbers & Quadratic Equations</div>
    <ul class="unit-topics">
      <li><span class="topic-name">Algebra of Complex Numbers:</span> Complex numbers as ordered pairs of reals, algebraic properties, Argand plane and polar representation. Modulus and conjugate of a complex number, triangle inequality. Fundamental theorem of algebra, solutions of quadratic equations with real coefficients in the complex number system, relation between roots and coefficients.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">Unit 3: Matrices and Determinants</div>
    <ul class="unit-topics">
      <li><span class="topic-name">Matrix Algebra:</span> Matrices, algebra of matrices, types of matrices, symmetric and skew-symmetric matrices, orthogonal matrices. Determinants of order up to 3x3, properties of determinants, minors, cofactors, adjoint and inverse of a matrix. Solution of systems of linear equations using Cramer's rule and matrix inverse method, consistency and inconsistency.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">Unit 4: Permutations, Combinations & Binomial Theorem</div>
    <ul class="unit-topics">
      <li><span class="topic-name">Combinatorics:</span> Fundamental principle of counting, factorial n, permutations and combinations, derivation of formulae for nPr and nCr, simple applications. Binomial theorem for positive integral index, general and middle terms, properties of binomial coefficients and applications.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">Unit 5: Sequences and Series</div>
    <ul class="unit-topics">
      <li><span class="topic-name">Progressions:</span> Arithmetic Progression (AP), arithmetic mean (AM), Geometric Progression (GP), general term of GP, sum of n terms of GP, infinite GP and its sum, geometric mean (GM), relation between AM and GM. Sum to n terms of special series: sum of n natural numbers, squares, and cubes.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">Unit 6: Mathematical Reasoning & Linear Inequalities</div>
    <ul class="unit-topics">
      <li><span class="topic-name">Logic:</span> Mathematically acceptable statements, connecting words/phrases "and", "or", "implies", "implied by", "if and only if". Validating statements using method of contradiction, contrapositive. Linear inequalities in one and two variables, graphical solution of systems of linear inequalities.</li>
    </ul>
  </div>

  <div class="sec-heading">Class XII Syllabus Modules</div>

  <div class="unit-card">
    <div class="unit-title">Unit 7: Limit, Continuity, and Differentiability</div>
    <ul class="unit-topics">
      <li><span class="topic-name">Differential Calculus:</span> Real-valued functions, algebra of functions, polynomials, rational, trigonometric, logarithmic and exponential functions. Inverse trigonometric functions and their properties. Limits, continuity, and differentiability. Derivative of sum, difference, product, and quotient of functions. Derivative of trigonometric, inverse trigonometric, logarithmic, exponential, composite and implicit functions; derivatives of order up to two. Rolle's and Lagrange's Mean Value Theorems.</li>
      <li><span class="topic-name">Applications of Derivatives:</span> Rate of change of quantities, monotonic increasing and decreasing functions, tangents and normals, maxima and minima of functions of one variable.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">Unit 8: Integral Calculus</div>
    <ul class="unit-topics">
      <li><span class="topic-name">Definite & Indefinite Integrals:</span> Fundamental integrals involving algebraic, trigonometric, exponential, and logarithmic functions. Integration by substitution, by parts, and by partial fractions. Integration using trigonometric identities. Fundamental theorem of calculus. Properties of definite integrals. Evaluation of definite integrals, determination of areas of regions bounded by simple curves in standard form.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">Unit 9: Differential Equations</div>
    <ul class="unit-topics">
      <li><span class="topic-name">Ordinary Differential Equations:</span> Ordinary differential equations, order and degree, formation of differential equations. Solution of differential equations by separation of variables method, solution of homogeneous and linear differential equations of first order (dy/dx + Py = Q).</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">Unit 10: Coordinate Geometry (2D and 3D)</div>
    <ul class="unit-topics">
      <li><span class="topic-name">Two-Dimensional Geometry:</span> Cartesian coordinate system in a plane, distance formula, section formula, locus. Slope of a line, parallel and perpendicular lines, intercepts of a line on coordinate axes. Various forms of equations of a line, intersection of lines, angles between two lines, distance of a point from a line. Standard forms of equations of a circle, radius, centre, equation of tangent. Conic sections: Parabola, ellipse, and hyperbola in standard forms, eccentricity, directrix, focus, and latus rectum.</li>
      <li><span class="topic-name">Three-Dimensional Geometry:</span> Coordinates of a point in space, distance between two points, section formula, direction cosines and direction ratios. Angle between two lines, skew lines, shortest distance between two lines. Equation of a line in space.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">Unit 11: Vector Algebra</div>
    <ul class="unit-topics">
      <li><span class="topic-name">Vectors:</span> Vectors and scalars, addition of vectors, components of a vector in 2D and 3D space, scalar multiplication, dot product, cross product, scalar and vector triple products, geometrical applications.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">Unit 12: Statistics and Probability</div>
    <ul class="unit-topics">
      <li><span class="topic-name">Descriptive Stats:</span> Measures of dispersion: calculation of mean, median, mode of grouped and ungrouped data; calculation of standard deviation, variance, and mean deviation for grouped and ungrouped data.</li>
      <li><span class="topic-name">Probability:</span> Probability of an event, addition and multiplication theorems of probability, Bayes' theorem, probability distribution of a random variable, Bernoulli trials, and binomial distribution.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">Unit 13: Trigonometry</div>
    <ul class="unit-topics">
      <li><span class="topic-name">Identities & Equations:</span> Trigonometric identities, functions, formulas for compound angles, multiple and sub-multiple angles. General solutions of trigonometric equations. Properties of triangles, inverse trigonometric functions and equations.</li>
    </ul>
  </div>
</body>
</html>
"""

# 4. CUSAT CAT PG MSc Mathematics Syllabus
def get_cusat_pg_mt_html():
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>CUSAT CAT - Post-Graduate M.Sc Mathematics Official Syllabus</title>
<style>{CSS}</style>
</head>
<body>
  <div class="header">
    <div class="inst-logo-sub">Cochin University of Science and Technology (CUSAT)</div>
    <h1>Post-Graduate Common Admission Test (PG CAT)</h1>
    <h2>Official Detailed Syllabus: M.Sc Mathematics (Test Code 611)</h2>
    <div class="badge-bar">
      <span class="badge">Program: M.Sc in Mathematics</span>
      <span class="badge">Level: Post-Graduate Entrance Examination</span>
      <span class="badge">Eligibility: B.Sc Mathematics Degree</span>
    </div>
  </div>

  <table class="pattern-table">
    <tr>
      <th>Parameter</th>
      <th>Examination Specification</th>
    </tr>
    <tr>
      <td><strong>Total Questions</strong></td>
      <td>150 Objective Multiple Choice Questions</td>
    </tr>
    <tr>
      <td><strong>Duration</strong></td>
      <td>2 Hours (120 Minutes)</td>
    </tr>
    <tr>
      <td><strong>Marking Scheme</strong></td>
      <td>+3 marks for correct response; -1 mark for incorrect response</td>
    </tr>
    <tr>
      <td><strong>Core Focus</strong></td>
      <td>Undergraduate (B.Sc) Mathematics core curriculum: Analysis, Algebra, Topology, Calculus, ODE/PDE</td>
    </tr>
  </table>

  <div class="unit-card">
    <div class="unit-title">1. Real Analysis</div>
    <ul class="unit-topics">
      <li>Real number system as a complete ordered field, Archimedean property, supremum, infimum.</li>
      <li>Sequences and series: convergence, limsup, liminf, Bolzano-Weierstrass theorem, Cauchy criterion, tests of convergence.</li>
      <li>Functions of single variable: limits, continuity, uniform continuity, intermediate value property.</li>
      <li>Differentiability, Mean Value Theorems, Taylor's theorem with remainder, maxima and minima.</li>
      <li>Riemann integration: partition, upper/lower sums, integrability criteria, fundamental theorem of calculus.</li>
      <li>Sequences and series of functions: pointwise and uniform convergence, Weierstrass M-test.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">2. Linear Algebra</div>
    <ul class="unit-topics">
      <li>Vector spaces, subspaces, linear dependence, linear independence, basis and dimension, coordinates.</li>
      <li>Linear transformations, rank-nullity theorem, matrix representations of linear transformations, change of basis.</li>
      <li>Systems of linear equations, Gauss elimination, determinants and properties.</li>
      <li>Eigenvalues, eigenvectors, characteristic polynomial, Cayley-Hamilton theorem, minimal polynomial.</li>
      <li>Diagonalizability, invariant subspaces, inner product spaces, Gram-Schmidt orthogonalization process, self-adjoint and unitary operators.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">3. Abstract Algebra</div>
    <ul class="unit-topics">
      <li>Group theory: groups, subgroups, cyclic groups, permutation groups, symmetric and alternating groups.</li>
      <li>Cosets, Lagrange's theorem, normal subgroups, quotient groups, group homomorphisms, isomorphism theorems.</li>
      <li>Automorphisms, Cayley's theorem, class equation, Sylow's theorems overview.</li>
      <li>Ring theory: rings, integral domains, division rings, fields, ideals, prime and maximal ideals, quotient rings.</li>
      <li>Homomorphisms of rings, polynomial rings, divisibility in integral domains, Euclidean domains, principal ideal domains (PID), unique factorization domains (UFD).</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">4. Complex Analysis</div>
    <ul class="unit-topics">
      <li>Algebra of complex numbers, geometric representation, analytic functions, Cauchy-Riemann equations, harmonic functions.</li>
      <li>Conformal mappings, Mobius (bilinear) transformations.</li>
      <li>Complex integration: contours, Cauchy-Goursat theorem, Cauchy's integral formula, Liouville's theorem, fundamental theorem of algebra.</li>
      <li>Taylor series, Laurent series, singularities, residues, Cauchy's residue theorem and evaluation of real integrals.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">5. Differential Equations (ODE & PDE)</div>
    <ul class="unit-topics">
      <li>First-order ordinary differential equations: exact, linear, Bernoulli, integrating factors.</li>
      <li>Higher-order linear differential equations with constant coefficients, method of undetermined coefficients, variation of parameters.</li>
      <li>Cauchy-Euler equations, system of linear differential equations.</li>
      <li>Partial differential equations: formation, first-order linear and quasilinear PDE, Lagrange's method, Charpit's method.</li>
      <li>Classification of second-order linear PDE: Laplace, wave, and heat equations in standard forms.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">6. Metric Spaces & General Topology</div>
    <ul class="unit-topics">
      <li>Metric spaces: open sets, closed sets, interior, closure, boundary, limit points.</li>
      <li>Completeness, Cantor intersection theorem, Baire category theorem.</li>
      <li>Continuous mappings between metric spaces, uniform continuity. Compactness, Heine-Borel theorem, connectedness and path-connectedness.</li>
      <li>Topological spaces: bases, subbases, subspace topology, product topology, Hausdorff spaces.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">7. Numerical Analysis, Vector Calculus & Probability</div>
    <ul class="unit-topics">
      <li>Numerical solutions of algebraic equations: bisection method, Newton-Raphson method, secant method.</li>
      <li>Interpolation: Lagrange interpolation, Newton's divided difference. Numerical integration: trapezoidal and Simpson's rules.</li>
      <li>Vector calculus: gradient, divergence, curl, line, surface and volume integrals, Green's, Stokes', and Gauss' divergence theorems.</li>
      <li>Probability: axioms of probability, conditional probability, Bayes theorem, random variables, expectation, variance, discrete and continuous distributions.</li>
    </ul>
  </div>
</body>
</html>
"""

def main():
    # Generate Physics Syllabi
    generate_pdf(get_cusat_ug_ph_html("2026"), "syllabus/CUSAT/PH/CUSAT_CAT_2026_Physics_Syllabus_and_Exam_Pattern.pdf")
    generate_pdf(get_cusat_ug_ph_html("2025"), "syllabus/CUSAT/PH/CUSAT_CAT_2025_Physics_Syllabus_and_Exam_Pattern.pdf")
    generate_pdf(get_cusat_ug_ph_html("2024"), "syllabus/CUSAT/PH/CUSAT_CAT_2024_Physics_Syllabus_and_Exam_Pattern.pdf")
    generate_pdf(get_cusat_ug_ph_html("Comprehensive"), "syllabus/CUSAT/PH/CUSAT_CAT_UG_Physics_Official_Syllabus.pdf")
    generate_pdf(get_cusat_pg_ph_html(), "syllabus/CUSAT/PH/CUSAT_CAT_PG_MSc_Physics_Official_Syllabus.pdf")

    # Generate Mathematics Syllabi
    generate_pdf(get_cusat_ug_mt_html("2026"), "syllabus/CUSAT/MT/CUSAT_CAT_2026_Mathematics_Syllabus_and_Exam_Pattern.pdf")
    generate_pdf(get_cusat_ug_mt_html("2025"), "syllabus/CUSAT/MT/CUSAT_CAT_2025_Mathematics_Syllabus_and_Exam_Pattern.pdf")
    generate_pdf(get_cusat_ug_mt_html("2024"), "syllabus/CUSAT/MT/CUSAT_CAT_2024_Mathematics_Syllabus_and_Exam_Pattern.pdf")
    generate_pdf(get_cusat_ug_mt_html("Comprehensive"), "syllabus/CUSAT/MT/CUSAT_CAT_UG_Mathematics_Official_Syllabus.pdf")
    generate_pdf(get_cusat_pg_mt_html(), "syllabus/CUSAT/MT/CUSAT_CAT_PG_MSc_Mathematics_Official_Syllabus.pdf")

if __name__ == '__main__':
    main()
