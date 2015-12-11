#Matt Layman - CS213 - substring3.py
def longest_substring(s, t):
    """Uses binary search to return k_substring of max length between s and t. Returns '' if no substring found."""
    best = ''                   #empty string if k_substring is None
    x = 0                       #min value
    y = min(len(s), len(t))     #max value
    z = (y-x)/2                 #midpoint

    while x<y:                                    #while min<max
        if k_substring(s, t, z) is not None:      #if substring exists of at least length midpoint(k>=z)
            x = z                                   #adjust min
            if x == y:                              #if min=max
                z = x                               #set k to max substring size
                break                               #exit loop
            z = (y + (x+1)) / 2                     #find new midpoint

        else:                                     #if substring length midpoint doesnt exist(k<z)
            y = z - 1                               #adjust max
            if x == y:                              #if min=max
                z = x                               #set k to max substring size
                break                               #exit loop
            z = (y + x) / 2                         #find new midpoint

    answer = k_substring(s, t, z)                 #run k_substring on max substring size k

    if answer is None:                            #if substring not found
        return best                               #return empty string
    else:
        return answer                             #else return substring

def k_substring(s, t, k):
    """Finds a substring of length k in both s and t if there is one,
    and returns it. Otherwise, returns None."""
    s_substrings = set()
    # Put all substrings of s of length k into a set: s_substrings
    for s_start in range(len(s)-k+1):
        current = s[s_start : s_start+k]
        s_substrings.add(current)
    # For every substring of t of length k, look for it in
    # s_substrings. If it's there, return it.
    for t_start in range(len(t)-k+1):
        current = t[t_start : t_start+k]
        if current in s_substrings:
            return current
    return None
