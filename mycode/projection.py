

def latlon_to_utm_zone(latitude, longitude):
    """
    Determine the UTM zone number and hemisphere for a given latitude and longitude.
    
    Parameters:
    - latitude (float): Latitude of the point in decimal degrees.
    - longitude (float): Longitude of the point in decimal degrees.
    
    Returns:
    - tuple: (UTM zone number, Hemisphere)
    """
    if not -180 <= longitude <= 180 or not -80 <= latitude <= 84:
        raise ValueError("Latitude must be between -80 and 84, and longitude between -180 and 180")
    
    zone = int((longitude + 180) / 6) + 1
    hemisphere = 'N' if latitude >= 0 else 'S'
    
    return zone, hemisphere