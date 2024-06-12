function solution(wallpaper) {
    let minLux = 99, minLuy = 99;
    let maxRdx = 0, maxRdy = 0;
    
    const width = wallpaper[0].length;
    const height = wallpaper.length;
    
    for (let i = 0; i < height; i++) {
        for (let j = 0; j < width; j++) {
            if (wallpaper[i][j] == '#') {
                minLux = Math.min(minLux, i);
                maxRdx = Math.max(maxRdx, i);
                minLuy = Math.min(minLuy, j);
                maxRdy = Math.max(maxRdy, j);
            }
        }
    }
    
    return [minLux, minLuy, maxRdx+1, maxRdy+1];
}