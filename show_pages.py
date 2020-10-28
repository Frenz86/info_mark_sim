import streamlit as st
import plotly.figure_factory as ff
from PIL import Image
import helpers
import pandas as pd
import numpy as np

def show_welcome_page():

    st.title("Welcome.")
    st.markdown("You will find the following in this section:")
    st.markdown("1. The History of Monte Carlo Method \n "
                "2. A High Level Montel Carlo Process \n"
                "3. An Interactive Example")
    st.markdown("If you are familiar with the basics, use the panel on the left to see some real-life examples.")

    # HISTORY
    st.markdown("***")
    st.markdown("** The Short History **")
    st.video("https://youtu.be/ioVccVC_Smg")

    # SIMULATION ARCHITECTURE
    st.markdown("***")
    st.markdown("** The Monte Carlo Process**")
    st.markdown("The goal of Monte Carlo Method is to **approximate an expected outcome** that is difficult to "
                "calculate precisely. In real life, it's often impossible to come up with a single equation to "
                "describe a system from inputs to outputs; even we can, it will be time consuming to "
                "calculate and analyze all possible outcome scenarios. "
                "As a practical alternative, Monte Carlo method allows us to take a **probability approach**.")

    image = Image.open('./image/monte-carlo-process.png')
    st.image(image, format='PNG', use_column_width=True)

    st.markdown("A more technical explanation ...")
    st.video("https://youtu.be/7TybpwBlcMk")


    # ILLUSTRATION OF PROBABILITY DISTRIBUTION
    st.markdown("***")
    st.markdown("**Step 1: Define input(s) with uncertainty ... **")

    value_range = st.slider("Pick the range of value that represent the input", min_value=20,
                       max_value=100, value=(45, 60), step=1)
    shape = st.selectbox("Pick a distribution that represent the uncertainty",
                         ("Normal", "Triangle", "Uniform"))
    N = st.slider("Choose how many samples (N): ", min_value=100, max_value=10000, value=500, step=100)

    st.markdown(f"We drew {N} samples "
                f"with an **uncertainty** represented by a **{shape}** distribution.")

    input_items = helpers.get_items(value_range, N, shape)

    hist_data = [input_items]
    group_label = ['Input']
    fig = ff.create_distplot(hist_data, group_label, bin_size=[0.5])
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("**Step 2: Apply Some Transformation ...**")
    distribution = st.selectbox("Pick a transformation",
                                ("Secret Formula 1", "Secret Formula 2", "Secret Formula 3"))
    st.markdown(f"We apply **{distribution}** (some non-linear functions and randomness) to each of the input samples ...")

    output_items = helpers.apply_function(input_items, distribution)
    hist_data = [output_items]
    group_label = ['Output']
    fig = ff.create_distplot(hist_data, group_label, bin_size=[0.1])
    st.plotly_chart(fig, use_container_width=True)

    # ANALYZE RESULTS
    st.markdown("**Step 3: Analyze the Outcome ...**")
    st.markdown("In this case, the results are not very sensible since it's a dummy example. "
                "Typically, we should ask the following quesitons: ")
    st.markdown("1. what is the probability of achieving the acceptable outcomes? Is it good enough to proceed? \n"
                "2. what is the probability of achieving sub-optimal outcomes? And how do we hedge against that? \n"
                "3. what factor has the largest impact on the outcome? How can we influence it? \n")

    st.markdown("***")



def show_ad_budget():

    # set up layout
    #st.title("Advertising Budget Simulator APP")
    st.markdown("Come responsabile marketing avrai la responsabilità "
                "di investire al meglio il budget per l'advertising in modo da massimizzare le vendite"
                "Gli obbiettivi sono i seguenti: ")
    st.markdown("1. Generare profitti minimo € 20.000 fino a € 50.000 per periodo di interesse \n"
                "2. Gestire meglio il prezzo di vendita, costi di produzione e vendita per ogni tipologia di prodotto\n"
                "3. Il goal è massimizzare il profitto su tutti i prodotti(sales revenue - cost)")

    st.markdown("La simulazione si compone in queste due parti principali: ")
    st.markdown("1. Come progettare una simulazione con **Influence Diagram** \n"
                "2. Come interpretare correttamente i risultati al fine di migliorare le business decision \n")
    
    st.markdown("** INFLUENCE DIAGRAM **")
    st.markdown("Il diagramma aiuta a concettualizzare i flussi: input, key factors, relazioni e risultati")

    st.markdown("Questi sono gli step fondamentali per creare l'Influence Diagram: ")
    st.markdown("1. Define a **quantitative objective** \n"
                "2. Identify the **controllable inputs** that are deterministic or with uncertainty \n"
                "3. Map out the **key factors** and relationships from inputs to output \n"
                "4. Identify the **non-trivial relationships** (e.g. f(x): advertising budget to unit sold) \n"
                "5. Get some **past data** to represent the factors and approximate the relationships; "
                "make sensible **assumptions** "
                "if needed (once you grasp the Monte Carlo concept, this step is arguably the most important. "
                "Garbage data & assumptions, garbage outcome.)")
    
    image = Image.open('./image/Influence-Diagram-Ad-Budget.png')
    st.image(image, caption='Influence Diagram of Ad Budget Problem', format='PNG',
             use_column_width=True)

    
    st.markdown("** SIMULAZIONE **")

    st.markdown("Prezzo di vendita e costi sono affetti da una certa **incertezza**. Possono essere controllati fino ad un certo punto, "
                "poichè per esempio, stagionalità ed la dipendenza dei costi dai diversi fornitori "
                "Ed è proprio qui che entra in gioco l'incertezza!")

    st.markdown("Scegliamo **le medie dei prezzi e costi** per le nostre simulazioni."
                "Ipotizziamo che le variabili costi e prezzi abbiano una distribuzione normale:")

    unit_price = st.slider(label="Scegliere il prezzo medio unitario",
                          max_value=50,
                          min_value=10,
                          step=1)

    unit_cost = st.slider(label="Scegliere il costo medio unitario",
                          max_value=40,
                          min_value=10,
                          step=1)

    st.markdown("Ora decidiamo quante simulazioni (e.g. _campagne_ marketing) vogliamo lanciare. "
                "In generale, più esperimenti lanciamo, più l'errore si ridurrà. Ma ricordiamo che aumentanfo troppo "
                "il numero degli esperimenti, i tempi di calcolo aumenteranno proporzionalmente.")

    N = st.slider(label="Number of experiment",
                          max_value=10000,
                          min_value=2500,
                          value=5000,
                          step=1000)

    price_item, cost_item = helpers.get_items_ad_triangular(unit_price, unit_cost, N)
    hist_data = [price_item, cost_item]
    group_label = ['Unit Price', 'Unit Cost']
    fig = ff.create_distplot(hist_data, group_label, bin_size=[0.5, 0.5], curve_type='normal')
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("Infine, scegliamo il **budget di advertising** per le nostre campagne. Trattasi di un fattore deterministico, poichè dipende esclusivamente da noi")
    ad_budget = st.slider(label="Scegliere l'Advertising Budget (€ x 1000)",
                          max_value=40,
                          min_value=5,
                          step=1)

    # Explain Transformation
    st.markdown("***")
    st.markdown("Seguendo Influence Diagram, conosciamo bene le relazioni tra le variabili di input ed output.")

    # Calculate Profit
    st.markdown("** OUTCOME **")
    st.markdown(f"Questo è l'andamento finale con **{N} simulazioni** ed un Advertising budget di **€{ad_budget*1000}** "
                f"per un  prezzo medio unitario di **€{unit_price}** e costi unitari di **€{unit_cost}**.")
    # Analysis
    st.markdown("** ANALISI **")
    st.markdown("Riportiamo sotto alcuni resoconti: ")
    profit_item, prob_profit = helpers.ad_calc_profit(price_item, cost_item, ad_budget)
    st.markdown(f"Utile medio: **€{sum(profit_item) / len(profit_item): .2f}**")
    st.markdown(f"Probabilità di break-even (ovvero per generare profitto positivo): **{prob_profit*100: .2f}%**")

    st.markdown(f"La redditività media dell'investimento (ROI) del Marketing Budget: "
            f"**{(sum(profit_item) / len(profit_item) - ad_budget*1000) *100 / (ad_budget*1000): .2f}%**")
    
    hist_data = [profit_item]
    group_label = ['estimated profit']
    fig = ff.create_distplot(hist_data, group_label, bin_size=[3000], curve_type='normal')
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("***")
    show_footer()


def pag2():

    # set up layout
    st.title("Welcome to the pag2")
    st.markdown("Coming soon ... Sign up [here]() to get notified.")
    show_footer()


def pag3():

    st.button("Re-run")
    # set up layout
    st.title("Welcome to the pag3")

def pag4():

    st.button("Re-run")
    # set up layout
    st.title("Welcome to the pag3")

##########################################################
#FOOTER
#########################################################
def show_footer():
    st.markdown("***")
    st.markdown("**Like this tool?** Seguici su: "
                "[Linkedin](https://www.linkedin.com/company/infomanager-srl/).")
