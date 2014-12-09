# EasyTeX Memorandum


### Header Fields
<table class="tg">
  <tr>
    <th class="tg-e3zv">Field Name</th>
    <th class="tg-e3zv">Required/Optional</th>
  </tr>
  <tr>
    <td class="tg-031e">author</td>
    <td class="tg-031e">Required</td>
  </tr>
  <tr>
    <td class="tg-031e">collaborators</td>
    <td class="tg-031e">Optional</td>
  </tr>
  <tr>
    <td class="tg-031e">date</td>
    <td class="tg-031e">Optional</td>
  </tr>
  <tr>
    <td class="tg-031e">title</td>
    <td class="tg-031e">Required</td>
  </tr>
  <tr>
    <td class="tg-031e">subtitle</td>
    <td class="tg-031e">Optional</td>
  </tr>
  <tr>
    <td class="tg-031e">packages</td>
    <td class="tg-031e">Optional</td>
  </tr>
</table>

### Sections
<table class="tg">
  <tr>
    <th class="tg-e3zv">Field Name</th>
    <th class="tg-e3zv">Required/Optional</th>
  </tr>
  <tr>
    <td class="tg-031e">title</td>
    <td class="tg-031e">Required</td>
  </tr>
  <tr>
    <td class="tg-031e">content</td>
    <td class="tg-031e">Required</td>
  </tr>
</table>

## General Layout
Note: all fields are left empty to illuminate EasyTeX's tabbed-delineation!

	memorandum:
		author:
		collaborators:
		date:
		title:
		subtitle:
		packages: 
		
		section:
			title:
			content:
				
		section:
			title:
			content: 

## Samples

### Memorandum with One Section (all optional fields filled)

	memorandum:
	    author: Paul Dapolito
	    collaborators: Robert, Angela, Daniel
	    date: 09/21/2015
	    title: Basic title
	    subtitle: Super \underline{Advanced} Subtitle
	    packages: graphicx

	    section:
	        title: Recording Recovery
	        content:
	            After a recording session with a pop singer, we were tasked with cleaning-up the corrupted audio track "popson
	            g.wav". As far as we understood, this audio track was recorded in our music studio for the pop singer. Upon
	            playing the sample after the recording session, we heard no audible song but significant high-frequency noise.
	            Unfortunately, it appeared that interference was injected into the recording. We thus set out to clean up the
	            sound recording using a non-causal filter in MATLAB and model a causal RC filter.

### Memorandum with Multiple Sections (some optional fields missing)

	memorandum:
	    author: Paul Dapolito
	    title: Analysis Using Ohm's Law

	    section:
	        title: Circuit Analysis
	        content:
	            From the circuit diagram in Figure 6, we used Ohm's Law to assert the following relation between the input
	            signal $V_{in}$ and the output signal $V_{out}$, where $i$ is the current in the circuit:
	                \begin{equation}
	                    \label{resistor equation}
	                    V_{in} - iR = V_{out}
	                \end{equation}

	            Because an ideal measuring device at the node labeled $V_{out}$ would draw no current, we can call the current
	            through both the resistor and capacitor equal. By the definition of impedence, we also know that $V_{out} -
	            iZ_{C} = 0$ where $Z_{C}$ is the impedence of the capacitor of capacitance $C$. We can express the impedence
	            of the capacitor $Z_{C}$ in terms of the angular frequency $\omega$ of the input and output signals such that:
	            \begin{equation}
	                \label{impedence equation}
	                Z_{C} = \frac{1}{j\omega C}
	            \end{equation}

	            Thus, from $V_{out} - iZ_{C} = 0$, we obtain
	            \begin{equation}
	                \label{first output voltage equation}
	                V_{out} = \frac{i}{j\omega C}
	            \end{equation}

	            Solving equation \ref{resistor equation} for the current $i$ of the circuit,
	            \begin{equation}
	                \label{current equation}
	                i=\frac{V_{in} - V_{out}}{R}
	            \end{equation}

	            Plugging equation \ref{current equation} into equation \ref{first output voltage equation}, and solving for
	            $V_{out}$:
	            \begin{equation}
	                \label{output voltage equation}
	                V_{out} = \frac{V_{in}}{1+R j \omega C}
	            \end{equation}

	            Equation \ref{output voltage equation} tells us that our circuit schematic diagram is a low-pass filter,
	            because $V_{out}$ decreases as the frequency $\omega$ of the input increases. We assumed a sinusoidal input
	            $V_{in} = a_i e^{j\omega t}$ and output  $V_{out} = a_o e^{j \omega t + \phi}$ where $\phi$ is the phase
	            shift between input and output signals. This was a safe assumption because any periodic signal can be
	            represented as a sum of sinusoids and our filter is a linear system. Plugging our expressions for $V_{in}$
	            and $V_{out}$ into equation \ref{output voltage equation}, solving for $\frac{V_{in}}{V_{out}}$, and
	            cancelling like terms, we obtain: 
	            \begin{equation}
	                \frac{a_i}{a_o} e^{-j \phi} = 1 + R j \omega C
	            \end{equation}

	            Applying Euler's identity, we find:
	            \begin{equation}
	                \label{using euler's identity}
	                \frac{a_i}{a_o} \left( \cos \phi - j \sin \phi \right ) = 1 + Rj \omega C
	            \end{equation}

	            Setting the real and imaginary parts of both sides of equation \ref{using euler's identity} equal, we obtain:
	            \begin{equation}
	                \label{trigonometric relations on phi}
	                \cos \phi = \frac{a_o}{a_i} \qquad \sin \phi = \frac{a_o}{a_i} (-R \omega C) \qquad \tan \phi = -R \omega C
	            \end{equation}

	            Thus, the phase-shift $\phi$ between input and output signals is given by:
	            \begin{equation}
	                \label{equation for phi}
	                \phi = \arctan(-R \omega C) 
	            \end{equation}

	            Equation \ref{trigonometric relations on phi} defines a right-triangle with sides $1$, $-R \omega C$, and
	            hypotenuse $\sqrt{1 + R^2 \omega^2 C^2}$. Manipulating equation \ref{trigonometric relations on phi}, we thus
	            have an expression for $\frac{a_o}{a_i}$:
	            \begin{equation}
	                \frac{a_o}{a_i} = \cos \phi = \frac{1}{\sqrt{1 + R^2 \omega^2 C^2}}
	            \end{equation}

	    section:
	        title: Transfer Function Derivation
	        content:
	            We have now obtained expressions for both the phase shift $\phi$ between the input and output signals as well
	            as the ratio of the signals' magnitudes $\frac{a_o}{a_i}$. The time constant $\tau$ for our circuit,
	            consisent with the time constant for any $RC$ circuit, is $\tau = RC$. As $\tau$ is the characteristic time
	            of our circuit, the characteristic angular frequency $\omega_c$ of the circuit, also known as the cutoff
	            angular frequency, is given by $\omega_c = \frac{1}{\tau}$. Converting angular frequency to frequency by
	            dividing by $2 \pi$, we found the cutoff frequency $f_c$ of our circuit to be:
	            \begin{equation}
	                \label{cutoff frequency equation}
	                f_c = \frac{1}{2 \pi \tau} = \frac{1}{2 \pi R C}
	            \end{equation}

	            Earlier, we decided that the cutoff frequency for the pop song signal should be one-half the maximum
	            frequency of the signal, which was roughly $11,025$ Hz. Reasonable values for the resistance $R$ of the
	            resistor in our circuit and the capacitance $C$ of the capacitor are $100 \Omega$ and $144$nF. These
	            resistance and capacitance values give the cutoff frequency $f_c$ as:
	            \begin{equation}
	                f_c = \frac{1}{2 \pi R C} = \frac{1}{2 \pi (100 \Omega) (144 \textrm{nF})} \approx 11052 \textrm{ Hz}
	            \end{equation}

	            We used a Bode plot in order to evaluate and analyze the limitations of our proposed filter. Manipulating
	            equation \ref{output voltage equation}, we find the transfer function $\frac{V_{out}}{V_{in}}$ of our circuit
	            to be:
	            \begin{equation}
	                \label{transfer function equation}
	                \frac{V_{out}}{V_{in}} = \frac{1}{1 + R j \omega C}
	            \end{equation}

	            A Bode magnitude plot plots the gain of the filter's transfer function against input signal frequency on a
	            log scale. The gain of the transfer function is defined as $20\log_{10}\frac{V_{out}}{V_{in}}$. Using our expression in equation \ref{transfer function equation} for the quantity $\frac{V_{out}}{V_{in}}$, we obtain (Cha \& Molinder, 223):
	            \begin{equation}
	                \label{gain equation}
	                \textrm{Gain} = 20\log_{10}\left | \frac{1}{1 + R j \omega C}\right |
	            \end{equation}

	            Computing the absolute value in equation \ref{gain equation}, we obtain an expression for the gain of the transfer function which does not include complex values:
	            \begin{equation}
	                \label{gain equation real}
	                \textrm{Gain} = 20\log_{10}\left (\frac{1}{\sqrt{1 + R^2 \omega^2 C^2}}\right ) = -10 \log_{10} (1 + R^2 \omega^2 C^2)
	            \end{equation}

