execfile("ADP - Data Collection.py")
execfile("Standard Atmosphere.py")

def airfoil(w0 = 404796.621304, wf = 166589.906793, ca = 10752, cv = 0.85):
    d = rmin(16)[1]
    rho = 804
    g = 9.81
    cv *= ((1.4 * 287 * atmos(ca)[0]) ** 0.5)
    print 'Cruise velocity: %s m/s' % cv
    wload = rmin(21)[1]
    print 'Wing Loading: %s N/m^2' % wload
    s = (w0 * g) / wload
    print 'Wing Area: %s m^2' % s
    ar = rmin(1)[1]
    print 'Aspect Ratio: %s (no unit)' % ar
    b = (ar * s) ** 0.5
    print 'Wing span: %s m' % b
    cavg = s / b
    print 'Average chord: %s (no unit)' % cavg
    tr = rmin(18)[1]
    print 'Taper Ratio: %s m' % tr
    cr = 2 * cavg / (tr + 1)
    print 'Root chord: %s m' % cr
    ct = tr * cr
    print 'Tip chord: %s (no unit)' % ct
    vf = wf / rho
    print 'Volume of fuel: %s m^3' % vf
    a0 = float(raw_input('Fuel to be stored in fuselage (in percent): ')) / 100
    a1 = float(raw_input('Allowance given to spars (in percent): ')) / 100
    a2 = float(raw_input('Allowance given to ribs (in percent): ')) / 100
    cmac = float(raw_input('Mean aerodynamic chord (no unit): '))
    tc = (vf - a0 * vf) / ((0.5 + a1) * cmac * cmac * (b / 2) * (0.5 + a2) * 0.75 * 2)
    print 'Thickness-to-chord ratio: %s (no unit)' % tc
    wl = w0 - 0.8 * wf
    print 'Landing Weight: %s N' % (wl * g)
    wc = (w0 + wl) / 2
    print 'Cruise Weight: %s N' % (wc * g)
    clc = 2 * wc * g / (atmos(ca)[2] * (cv ** 2) * s)
    print 'Lift coefficient at cruise: %s (no unit)' % clc
    u = (2 * 0.2 * g * 0.6 * d) ** 0.5
    print 'Landing speed: %s m/s' % u
    vs = u / 1.2
    print 'Stalling speed: %s m/s' % vs
    clm = 2 * wl * g / (1.225 * (vs ** 2) * s)
    print 'Maximum Lift coefficient: %s (no unit)' % clm
    delta = clm - clc
    print 'Lift coefficient change required: %s (no unit)' % delta
