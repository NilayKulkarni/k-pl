import plotly.plotly as py
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_ebola.csv')
df.head()

cases = []
colors = ['rgb(239,243,255)','rgb(189,215,231)','rgb(107,174,214)','rgb(33,113,181)']
months = {6:'June',7:'July',8:'Aug',9:'Sept'}

for i in range(6,10)[::-1]:
    cases.append( dict(
        type = 'scattergeo',
        lon = df[ df['Month'] == i ]['Lon'], #-(max(range(6,10))-i), 
        lat = df[ df['Month'] == i ]['Lat'], 
        text = df[ df['Month'] == i ]['Value'], 
        sizemode = 'diameter',
        name = months[i],
        marker = dict( 
            size = df[ df['Month'] == i ]['Value']/50, 
            color = colors[i-6],
            line = dict(width = 0)
        ),
        tick0 = 0,
        zmin = 0,
        dtick = 1000,
        colorbar = dict(
            autotick = False,
            tickprefix = '',
            title = ''
        ),
    ) )

cases[0]['text'] = df[ df['Month'] == 9 ]['Value'].map('{:.0f}'.format).astype(str)+' '+\
    df[ df['Month'] == 9 ]['Country']
cases[0]['mode'] = 'markers+text'
cases[0]['textposition'] = 'bottom center'
    
inset = [ 
    dict(
        type = 'choropleth',
        locationmode = 'country names',
        locations = df[ df['Month'] == 9 ]['Country'],
        z = df[ df['Month'] == 9 ]['Value'],
        text = df[ df['Month'] == 9 ]['Country'],
        colorscale = [[0,'rgb(0, 0, 0)'],[1,'rgb(0, 0, 0)']],
        autocolorscale = False,
        showscale = False,
        geo = 'geo2'
    ),
    dict(
        type = 'scattergeo',
        lon = [19.999322], 
        lat = [73.790102], 
        text = ['Africa'], 
        mode = 'text',
        showlegend = False,
        geo = 'geo2'
    )
]

layout = dict(
    title = 'Ebola cases reported by month in West Africa 2014<br> \
Source: <a href="https://data.hdx.rwlabs.org/dataset/rowca-ebola-cases">\
HDX</a>',
    geo = dict(
        resolution = 50,
        showframe = False,
        showcoastlines = True,
        showland = True,
        landcolor = "rgb(229, 229, 229)",
        countrycolor = "rgb(255, 255, 255)" ,
        coastlinecolor = "rgb(255, 255, 255)",
        projection = dict(
            type = 'Mercator'
        ),
        lonaxis = dict(range=[20.002871, 73.880053]),
        lataxis = dict(range=[20.032225, 73.790445]),
        domain = dict( 
            x = [ 0, 1 ],
            y = [ 0, 1 ]
        )        
    ),
    geo2 = dict(
        showframe = False,
        showland = True,
        landcolor = "rgb(229, 229, 229)",
        domain = dict( 
            x = [ 0, 0.6 ],
            y = [ 0, 0.6 ]
        ),
        bgcolor = 'rgba(255, 255, 255, 0.0)',
    ),
    legend = dict(
           traceorder = 'reversed'
    )
)

fig = { 'layout':layout, 'data':cases+inset }
url = py.plot( fig, validate=False, filename='West Africa Ebola cases 2014' )