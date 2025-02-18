def plot_ideam(lista_codigos_requeridos):
    import cartopy.crs as ccrs
    import matplotlib.pyplot as plt
    import cartopy
    import geopandas as gpd
    import os

    ruta_py=os.getcwd()
    ruta_gpd_estaciones='\\'.join(ruta_py.split('\\')[:-1])+'\\0_ARCHIVOS_SIG\Estaciones_IDEAM_MAGNA_Colombia.shp'
    print('!NOTA Ubicacion shp= '+ruta_gpd_estaciones)
    gpd_estaciones=gpd.read_file(ruta_gpd_estaciones)
    gpd_estaciones=gpd_estaciones.to_crs('EPSG:4326')
    gpd_estaciones['Codigo']=gpd_estaciones['Codigo'].astype(int)
    gpd_estaciones_requeridas=gpd_estaciones[gpd_estaciones['Codigo'].isin(lista_codigos_requeridos[0])]
    #gpd_estaciones_disponibles=gpd_estaciones[gpd_estaciones['Codigo'].isin(lista_estaciones_recibidas[0])]

    fig = plt.figure(figsize=(15, 8))
    ax = plt.axes(projection=ccrs.PlateCarree())
    gpd_estaciones.plot(ax=ax,color='gray',label='Est todas',markersize=0.8)
    #gpd_estaciones_disponibles.plot(ax=ax,color='green',label='Est Disp',markersize=0.8)
    gpd_estaciones_requeridas.plot(ax=ax,color='r',label='Est select',markersize=0.8)
    #ax.add_feature(cartopy.feature.LAND)
    ax.add_feature(cartopy.feature.OCEAN)
    ax.add_feature(cartopy.feature.COASTLINE)
    ax.add_feature(cartopy.feature.BORDERS, linestyle='-', alpha=.5)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.95)
    ax.add_feature(cartopy.feature.RIVERS)
    ax.gridlines(draw_labels=True,crs=ccrs.PlateCarree(), color='k', linestyle=(0, (1, 5)))
    #ctx.add_basemap(ax, crs=gpd_estaciones.crs)
    ax.legend(ncol=1, loc='lower left')
    plt.show()

