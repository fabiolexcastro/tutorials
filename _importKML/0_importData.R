
require(raster)
require(rgdal)
require(plotKML)
require(maptools)
require(XML)

# Agosto 2 2017

files <- list.files('_data/_gdb', full.names = T, pattern = '.gdb')
list  <- lapply(files, FUN = ogrListLayers)

poly  <- list()
poly_cnts <- list()
cnts_p <- list() 

for(i in 1:length(files)){
  
  poly[[i]] <- readOGR(dsn = files[[i]], layer = as.character(list[[i]][1]))
  
  if(!file.exists(paste0('/_data/_shp/', gsub(' ', '', as.character(poly[[i]]@data[1,1])), '.shp'))){
    
    writeOGR(obj = poly[[i]], dsn = '_data/_shp', layer = gsub(' ', '', as.character(poly[[i]]@data[1,1])), driver = 'ESRI Shapefile')
    print('Written Shapefiles')
    
  } 
  
}

