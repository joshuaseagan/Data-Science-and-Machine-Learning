from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import geopandas as gpd
import pandas as pd
from pathlib import Path

#importdatasets
year2000 = pd.read_csv(r'/Users/annikasubido/Downloads/Final Project/DATA101-S11-GROUP 3-FINAL PROJECT/2000.csv')
year2015 = pd.read_csv(r'/Users/annikasubido/Downloads/Final Project/DATA101-S11-GROUP 3-FINAL PROJECT/2015.csv')
year2000_main = pd.read_csv(r'/Users/annikasubido/Downloads/Final Project/DATA101-S11-GROUP 3-FINAL PROJECT/2000main.csv')
year2015_main = pd.read_csv(r'/Users/annikasubido/Downloads/Final Project/DATA101-S11-GROUP 3-FINAL PROJECT/2015main.csv')
areadata = pd.read_csv(r'/Users/annikasubido/Downloads/Final Project/DATA101-S11-GROUP 3-FINAL PROJECT/areadata.csv')
scatterdata = pd.read_csv(r'/Users/annikasubido/Downloads/Final Project/DATA101-S11-GROUP 3-FINAL PROJECT/RegionPopandGDP.csv')
scatterdata_main=pd.read_csv(r'/Users/annikasubido/Downloads/Final Project/DATA101-S11-GROUP 3-FINAL PROJECT/scatter-main.csv')

#import shp
for_merge2000 = gpd.read_file(r'/Users/annikasubido/Downloads/Final Project/DATA101-S11-GROUP 3-FINAL PROJECT/regions_2000.shp').set_index('name')
for_merge2015 = gpd.read_file(r'/Users/annikasubido/Downloads/Final Project/DATA101-S11-GROUP 3-FINAL PROJECT/regions_2015.shp').set_index('name')

#for main page
gvaattributes2000 = pd.read_csv(r'/Users/annikasubido/Downloads/Final Project/DATA101-S11-GROUP 3-FINAL PROJECT/gva2000.csv')
gvaattributes2015 = pd.read_csv(r'/Users/annikasubido/Downloads/Final Project/DATA101-S11-GROUP 3-FINAL PROJECT/gva2015.csv')

#for sectoral
attributes2000 = pd.read_csv(r'/Users/annikasubido/Downloads/Final Project/DATA101-S11-GROUP 3-FINAL PROJECT/attributes2000.csv')
attributes2015 = pd.read_csv(r'/Users/annikasubido/Downloads/Final Project/DATA101-S11-GROUP 3-FINAL PROJECT/attributes2015.csv')

#merging
for_gva2000 = for_merge2000.merge(gvaattributes2000, on='region', how='left')
for_gva2015 = for_merge2015.merge(gvaattributes2000, on='region', how='left')

for_trim2000 = for_merge2000.merge(attributes2000, on='region', how='left')
for_trim2015 = for_merge2015.merge(attributes2015, on='region', how='left')

#mainpage trim
gva_df2000 = for_gva2000[['region','geometry','agri_y', 'manu_y', 'services_y']]
gva_df2000.columns = ['Region', 'Geometry', 'Agriculture', 'Manufacturing', 'Services']

gva_df2015 = for_gva2015[['region','geometry','agri_y', 'manu_y', 'services_y']]
gva_df2015.columns = ['Region', 'Geometry', 'Agriculture', 'Manufacturing', 'Services']

#sectoral trim
geo_df2000 = for_trim2000[['region','geometry','agri_y', 'manu_y', 'services_y']]
geo_df2000.columns = ['Region', 'Geometry', 'Agriculture', 'Manufacturing', 'Services']

geo_df2015 = for_trim2015[['region','geometry','agri_y', 'manu_y', 'services_y']]
geo_df2015.columns = ['Region', 'Geometry', 'Agriculture', 'Manufacturing', 'Services']

#last for main page
gva_df2000['dominant_sector'] = gva_df2000[['Agriculture', 'Manufacturing', 'Services']].idxmax(axis=1)
gva_df2015['dominant_sector'] = gva_df2015[['Agriculture', 'Manufacturing', 'Services']].idxmax(axis=1)

#mergingotherdata
year2000areamerged = pd.merge(year2000, areadata, on='REGN', how='inner')
year2015areamerged = pd.merge(year2015, areadata, on='REGN', how='inner')
agri2000density = year2000areamerged.set_index("Agriculture")
agri2015density = year2015areamerged.set_index("Agriculture")
manu2000density = year2000areamerged.set_index("Manufacturing")
manu2015density = year2015areamerged.set_index("Manufacturing")
serv2000density = year2000areamerged.set_index("Services")
serv2015density = year2015areamerged.set_index("Services")

px.set_mapbox_access_token(open(".mapbox_token").read())

# Initializing your Dash application
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

#Layout
app.layout = html.Div(children=[
    dbc.Container(fluid=True, style ={'margin': '10px'}, children=[
        dbc.Row(children=[
            html.H1("Visualizing Employment Densities by Region in the Philippines", style={'textAlign': 'center'})
        ]),
        dbc.Row(children=[
            html.P("This dashboard provides a thorough overview of the employment densities by sector in numerous regions in the country, enabling you to dive deeper into regional workforce dynamics with clarity and precision.", style={'textAlign': 'center'}),
            html.Br(),
            html.Br(),
        ]),
        dbc.Row(children=[
            dbc.Col(children=[
                #For description & pie chart
                dbc.Row(children=[dcc.Loading(id="pie-loading", children=dcc.Graph(id="pie-graph"))]),
                dbc.Row(id="extra-description")
            ], width=4),
            dbc.Col(children=[
                #For radio buttons and choropleth
                dbc.Row(style={'textAlign': 'center'}, children = [
                    dcc.RadioItems(['2000', '2015'], '2000', id='year-select', inline=True, labelStyle={'margin-right': '50px'})
                ]),
                dbc.Row(children = [
                    dcc.Loading(id="map-loading", children=dcc.Graph(id="map-graph")),
                ]),
            ], width=4),
            dbc.Col(children=[
                #For dropdown, bar, and scatterplot
                dbc.Row(children = [
                    dcc.Dropdown(['Main Page','Agriculture','Manufacturing','Services'], 'Main Page', id="sector-select")
                ]),
                dbc.Row(children = [
                    dcc.Loading(id="bar-loading", children=dcc.Graph(id="bar-graph")),
                ]),
                dbc.Row(children = [
                    dcc.Loading(id="scatter-loading", children=dcc.Graph(id="scatter-plot"))
                ]),
            ], width=4),
        ])
    ])
])

@callback(
    Output('map-graph', 'figure'),
    Output('pie-graph','figure'),
    Output('bar-graph','figure'),
    Output('scatter-plot','figure'),
    Output('extra-description','children'),
    Input('year-select', 'value'),
    Input('sector-select', 'value')
)
def update_all_graphs(selected_year, selected_sector):
    text = html.P("")
    if '2000' == selected_year:
        if 'Agriculture' == selected_sector:
            map_fig = px.choropleth_mapbox(geo_df2000, geojson=geo_df2000.Geometry, locations=geo_df2000.index, color='Agriculture', center={'lat': 12.099568, 'lon': 122.733168}, zoom=4,height=800, title="Employment Density per Region, 2000", color_continuous_scale=px.colors.sequential.algae)
            bar_fig=px.bar(year2000,x="REGN",y="Agriculture",color_discrete_sequence=["#1b9e77"],labels=dict(REGN="Region", Agriculture="Employed Persons"),title="Employment in the Agricultural Sector per Region, 2000")
            pie_fig=px.pie(agri2000density,values=agri2000density.index, names='REGN',color_discrete_sequence=px.colors.sequential.algae_r,title="Employment Density, Agriculture, per Region, 2000")
            scatter_fig=px.scatter(scatterdata, x="GDP per Capita, 2000", y="Employment Share, 2000, Agriculture", color="REGION", hover_data=['Employment Share, 2000, Agriculture'],color_discrete_sequence=px.colors.qualitative.Prism, title="GDP per Capita vs. Employment Share of Agriculture, 2000")
            text = html.P([
                "Agriculture comprises all workers in (1) agriculture, (2) forestry, and (3) fishing.",
                html.Br(),
                html.Br(),
                "In 2000, the ",
                html.Span(("top 5 regions in the Agricultural Sector"), style={'textDecoration': 'underline'}),
                " according to employment density are:",
                html.Br(),
                "1. CALABARZON & MIMAROPA (formerly Region 4)",
                html.Br(),
                "2. Western Visayas",
                html.Br(),
                "3. Southern Mindanao",
                html.Br(),
                "4. Central Visayas",
                html.Br(),
                "5. Bicol"
                ])
        if 'Manufacturing' == selected_sector:
            map_fig = px.choropleth_mapbox(geo_df2000, geojson=geo_df2000.Geometry, locations=geo_df2000.index, color='Manufacturing', center={'lat': 12.099568, 'lon': 122.733168}, zoom=4,height=800, title="Employment Density per Region, 2000", color_continuous_scale=px.colors.sequential.Oranges)
            bar_fig=px.bar(year2000,x="REGN",y="Manufacturing",color_discrete_sequence=["#d95f02"],labels=dict(REGN="Region", Manufacturing="Employed Persons"),title="Employment in the Manufacturing Sector per Region, 2000")
            pie_fig=px.pie(manu2000density,values=manu2000density.index, names='REGN',color_discrete_sequence=px.colors.sequential.Oranges_r,title="Employment Density, Manufacturing, per Region, 2000")
            scatter_fig=px.scatter(scatterdata, x="GDP per Capita, 2000", y="Employment Share, 2000, Manufacturing",color="REGION", hover_data=['Employment Share, 2000, Manufacturing'],color_discrete_sequence=px.colors.qualitative.Prism,title="GDP per Capita vs. Employment Share of Manufacturing, 2000")
            text = html.P([
                "Manufacturing comprises all workers in (1) mining and quarrying, (2) manufacturing, (3) electricity, steam, water, and waste management, and (4) construction.",
                html.Br(),
                html.Br(),
                "In 2000, the ",
                html.Span(("top 5 regions in the Manufacturing Sector"), style={'textDecoration': 'underline'}),
                " according to employment density are:",
                html.Br(),
                "1. CALABARZON & MIMAROPA (formerly Region 4)",
                html.Br(),
                "2. NCR",
                html.Br(),
                "3. Central Luzon",
                html.Br(),
                "4. Central Visayas",
                html.Br(),
                "5. Western Visayas"
                ])
        if 'Services' == selected_sector:
            map_fig = px.choropleth_mapbox(geo_df2000, geojson=geo_df2000.Geometry, locations=geo_df2000.index, color='Services', center={'lat': 12.099568, 'lon': 122.733168}, zoom=4,height=800, title="Employment Density per Region, 2000", color_continuous_scale=px.colors.sequential.Purples)
            bar_fig=px.bar(year2000,x="REGN",y="Services",color_discrete_sequence=["#7570b3"],labels=dict(REGN="Region", Services="Employed Persons"),title="Employment in the Services Sector per Region, 2000")
            pie_fig=px.pie(serv2000density,values=serv2000density.index, names='REGN',color_discrete_sequence=px.colors.sequential.Purples_r,title="Employment Density, Services, per Region, 2000")
            scatter_fig=px.scatter(scatterdata, x="GDP per Capita, 2000", y="Employment Share, 2000, Services",color="REGION", hover_data=['Employment Share, 2000, Services'],color_discrete_sequence=px.colors.qualitative.Prism,title="GDP per Capita vs. Employment Share of Services, 2000")
            text = html.P([
                "Services comprises all workers under (1) wholesale and retail trade; repair of motor vehicles and motorcycles, (2) transportation and storage, (3) accommodation and food service activities, (4) information and communication, (5) financial and insurance activities, (6) real estate and ownership of dwellings, (7) professional and business services, (8) public administration and defense; compulsory social activities, (9) education, (10) human health and social work activities, and (11) other services).",
                html.Br(),
                html.Br(),
                "In 2000, the ",
                html.Span(("top 5 regions in the Services Sector"), style={'textDecoration': 'underline'}),
                " according to employment density are:",
                html.Br(),
                "1. NCR",
                html.Br(),
                "2. CALABARZON & MIMAROPA (formerly Region 4)",
                html.Br(),
                "3. Central Luzon",
                html.Br(),
                "4. Southern Mindanao",
                html.Br(),
                "5. Western Visayas"
                ])
        elif 'Main Page' == selected_sector:
            map_fig = px.choropleth_mapbox(gva_df2000, geojson=gva_df2000.Geometry, locations=gva_df2000.index, color='dominant_sector', center={'lat': 12.099568, 'lon': 122.733168}, zoom=4,height=800, title="Gross Value Added per Region, 2000")
            bar_fig=px.bar(year2000,x='REGN',y=['Agriculture','Manufacturing','Services'],color_discrete_sequence=["#1b9e77", "#d95f02", "#7570b3"],
                           labels={
                               'REGN': "Region",
                               'value': "Employed Persons",
                               'variable':"Sector"},
                            title="Number of Employed Persons by Sector per Region, 2000",
                            barmode = "stack")
            pie_fig=px.pie(year2000_main,values='Total', names='Sector',color_discrete_sequence=["#7570b3","#1b9e77", "#d95f02"],title="Employment by Sector, 2000")
            scatter_fig=px.scatter(scatterdata_main, x="GDP per Capita, 2000", y="Total Workers, 2000",color="REGION", hover_data=['Total Workers, 2000'],color_discrete_sequence=px.colors.qualitative.Prism, title="GDP per Capita vs. Total Workers, 2000")
            text = html.P([
                        "Agriculture comprises all workers in (1) agriculture, (2) forestry, and (3) fishing.",
                        html.Br(),
                        html.Br(),
                        "Manufacturing comprises all workers in (1) mining and quarrying, (2) manufacturing, (3) electricity, steam, water, and waste management, and (4) construction.",
                        html.Br(),
                        html.Br(),
                        "Services comprises all workers under (1) wholesale and retail trade; repair of motor vehicles and motorcycles, (2) transportation and storage, (3) accommodation and food service activities, (4) information and communication, (5) financial and insurance activities, (6) real estate and ownership of dwellings, (7) professional and business services, (8) public administration and defense; compulsory social activities, (9) education, (10) human health and social work activities, and (11) other services."
                        ])
    elif '2015' == selected_year:
        if 'Agriculture' == selected_sector:
            map_fig = px.choropleth_mapbox(geo_df2015, geojson=geo_df2015.Geometry, locations=geo_df2015.index, color='Agriculture', center={'lat': 12.099568, 'lon': 122.733168}, zoom=4,height=800, title="Employment Density per Region, 2015", color_continuous_scale=px.colors.sequential.algae)
            bar_fig=px.bar(year2015,x="REGN",y="Agriculture",color_discrete_sequence=["#1b9e77"],labels=dict(REGN="Region", Agriculture="Employed Persons"),title="Employment in the Agricultural Sector per Region, 2015")
            pie_fig=px.pie(agri2015density,values=agri2015density.index, names='REGN',color_discrete_sequence=px.colors.sequential.algae_r,title="Employment Density, Agriculture, per Region, 2015")
            scatter_fig=px.scatter(scatterdata, x="GDP per Capita, 2015", y="Employment Share, 2015, Agriculture",color="REGION", hover_data=['Employment Share, 2015, Agriculture'],color_discrete_sequence=px.colors.qualitative.Prism,title="GDP per Capita vs. Employment Share of Agriculture, 2015")
            text = html.P([
                "Agriculture comprises all workers in (1) agriculture, (2) forestry, and (3) fishing.",
                html.Br(),
                html.Br(),
                "In 2015, the ",
                html.Span(("top 5 regions in the Agricultural Sector"), style={'textDecoration': 'underline'}),
                " according to employment density are:",
                html.Br(),
                "1. Western Visayas",
                html.Br(),
                "2. Central Mindanao",
                html.Br(),
                "3. Central Visayas",
                html.Br(),
                "4. Bicol",
                html.Br(),
                "5. Central Luzon"
                ])
        if 'Manufacturing' == selected_sector:
            map_fig = px.choropleth_mapbox(geo_df2015, geojson=geo_df2015.Geometry, locations=geo_df2015.index, color='Manufacturing', center={'lat': 12.099568, 'lon': 122.733168}, zoom=4,height=800, title="Employment Density per Region, 2015", color_continuous_scale=px.colors.sequential.Oranges)
            bar_fig=px.bar(year2015,x="REGN",y="Manufacturing",color_discrete_sequence=["#d95f02"],labels=dict(REGN="Region", Manufacturing="Employed Persons"),title="Employment in the Manufacturing Sector per Region, 2015")
            pie_fig=px.pie(manu2015density,values=manu2015density.index, names='REGN',color_discrete_sequence=px.colors.sequential.Oranges_r,title="Employment Density, Manufacturing, per Region, 2015")
            scatter_fig=px.scatter(scatterdata, x="GDP per Capita, 2015", y="Employment Share, 2015, Manufacturing",color="REGION", hover_data=['Employment Share, 2015, Manufacturing'],color_discrete_sequence=px.colors.qualitative.Prism,title="GDP per Capita vs. Employment Share of Manufacturing, 2015")
            text = html.P([
                "Manufacturing comprises all workers in (1) mining and quarrying, (2) manufacturing, (3) electricity, steam, water, and waste management, and (4) construction.",
                html.Br(),
                html.Br(),
                "In 2015, the ",
                html.Span(("top 5 regions in the Manufacturing Sector"), style={'textDecoration': 'underline'}),
                " according to employment density are:",
                html.Br(),
                "1. CALABARZON",
                html.Br(),
                "2. Central Luzon",
                html.Br(),
                "3. NCR",
                html.Br(),
                "4. Central Visayas",
                html.Br(),
                "5. Western Visayas"
                ])
        if 'Services' == selected_sector:
            map_fig = px.choropleth_mapbox(geo_df2015, geojson=geo_df2015.Geometry, locations=geo_df2015.index, color='Services', center={'lat': 12.099568, 'lon': 122.733168}, zoom=4,height=800, title="Employment Density per Region, 2015", color_continuous_scale=px.colors.sequential.Purples)
            bar_fig=px.bar(year2015,x="REGN",y="Services",color_discrete_sequence=["#7570b3"],labels=dict(REGN="Region", Services="Employed Persons"),title="Employment in the Services Sector per Region, 2015")   
            pie_fig=px.pie(serv2015density,values=serv2015density.index, names='REGN',color_discrete_sequence=px.colors.sequential.Purples_r,title="Employment Density, Services, per Region, 2015")
            scatter_fig=px.scatter(scatterdata, x="GDP per Capita, 2015", y="Employment Share, 2015, Services",color="REGION", hover_data=['Employment Share, 2015, Services'],color_discrete_sequence=px.colors.qualitative.Prism,title="GDP per Capita vs. Employment Share of Services, 2015")
            text = html.P([
                "Services comprises all workers under (1) wholesale and retail trade; repair of motor vehicles and motorcycles, (2) transportation and storage, (3) accommodation and food service activities, (4) information and communication, (5) financial and insurance activities, (6) real estate and ownership of dwellings, (7) professional and business services, (8) public administration and defense; compulsory social activities, (9) education, (10) human health and social work activities, and (11) other services).",
                html.Br(),
                html.Br(),
                "In 2015, the ",
                html.Span(("top 5 regions in the Services Sector"), style={'textDecoration': 'underline'}),
                " according to employment density are:",
                html.Br(),
                "1. NCR",
                html.Br(),
                "2. CALABARZON",
                html.Br(),
                "3. Central Luzon",
                html.Br(),
                "4. Western Visayas",
                html.Br(),
                "5. Central Visayas"
                ])
        elif 'Main Page' == selected_sector:
            map_fig = px.choropleth_mapbox(gva_df2015, geojson=gva_df2015.Geometry, locations=gva_df2015.index, color='dominant_sector', center={'lat': 12.099568, 'lon': 122.733168}, zoom=4,height=800, title="Gross Value Added per Region, 2015")
            bar_fig=px.bar(year2015,x='REGN',y=['Agriculture','Manufacturing','Services'],color_discrete_sequence=["#1b9e77", "#d95f02", "#7570b3"],
                           labels={
                               'REGN': "Region",
                               'value': "Employed Persons",
                               'variable':"Sector"},
                            title="Number of Employed Persons by Sector per Region, 2015",
                            barmode = "stack")
            pie_fig=px.pie(year2015_main,values='Total', names='Sector',color_discrete_sequence=["#7570b3","#1b9e77", "#d95f02"],title="Employment by Sector, 2015")
            scatter_fig=px.scatter(scatterdata_main, x="GDP per Capita, 2015", y="Total Workers, 2015",color="REGION", hover_data=['Total Workers, 2015'],color_discrete_sequence=px.colors.qualitative.Prism, title="GDP per Capita vs. Total Workers, 2015")
            text = html.P([
                        "Agriculture comprises all workers in (1) agriculture, (2) forestry, and (3) fishing.",
                        html.Br(),
                        html.Br(),
                        "Manufacturing comprises all workers in (1) mining and quarrying, (2) manufacturing, (3) electricity, steam, water, and waste management, and (4) construction.",
                        html.Br(),
                        html.Br(),
                        "Services comprises all workers under (1) wholesale and retail trade; repair of motor vehicles and motorcycles, (2) transportation and storage, (3) accommodation and food service activities, (4) information and communication, (5) financial and insurance activities, (6) real estate and ownership of dwellings, (7) professional and business services, (8) public administration and defense; compulsory social activities, (9) education, (10) human health and social work activities, and (11) other services."
                        ])

    return map_fig, pie_fig, bar_fig, scatter_fig, text




if __name__ == '__main__':
    app.run(debug=True)