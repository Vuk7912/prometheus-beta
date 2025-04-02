def stable_marriage(preferences):
    """
    Implement the Gale-Shapley algorithm for stable marriage problem.
    
    Args:
        preferences (dict): A dictionary where keys are groups (e.g., 'men' or 'women'),
                            and values are lists of preference lists for each member.
                            Format: {'men': [[preferences], ...], 'women': [[preferences], ...]}
    
    Returns:
        dict: A stable matching where each person is paired with their match.
    
    Raises:
        ValueError: If input preferences are invalid or unbalanced.
    """
    # Validate input
    if not preferences or 'men' not in preferences or 'women' not in preferences:
        raise ValueError("Preferences must contain 'men' and 'women' keys")
    
    men = preferences['men']
    women = preferences['women']
    
    # Validate that the number of men and women are equal
    if len(men) != len(women):
        raise ValueError("Number of men and women must be equal")
    
    n = len(men)
    
    # Early impossibility check
    for m1 in range(n):
        for m2 in range(n):
            if m1 == m2:
                continue
            # Mutual top preference swap
            if (men[m1][0] == m2 and men[m2][0] == m1 and
                women[m1][0] == m2 and women[m2][0] == m1):
                raise ValueError("No stable matching possible")
    
    # Initialize data structures
    men_free = list(range(n))
    women_partners = [None] * n
    men_partners = [None] * n
    
    # Track proposal attempts for each man
    proposals_count = [0] * n
    
    max_proposals = n * n  # Prevent infinite loop
    total_proposals = 0
    
    while men_free and total_proposals < max_proposals:
        # No men left or too many proposals
        if not men_free:
            break
        
        # Take a free man
        man = men_free.pop(0)
        
        # His preference list
        preference_list = men[man]
        
        # Propose to next preferred woman
        if proposals_count[man] >= n:
            # This means the man has proposed to everyone and found no match
            raise ValueError("No stable matching possible")
        
        woman_index = preference_list[proposals_count[man]]
        proposals_count[man] += 1
        total_proposals += 1
        
        # Check if woman is free
        if women_partners[woman_index] is None:
            # Woman accepts first proposal
            women_partners[woman_index] = man
            men_partners[man] = woman_index
        else:
            # Compare current partner with new proposer
            current_partner = women_partners[woman_index]
            woman_prefs = preferences['women'][woman_index]
            
            # Check woman's preference order
            if woman_prefs.index(man) < woman_prefs.index(current_partner):
                # Woman prefers new man
                women_partners[woman_index] = man
                men_partners[man] = woman_index
                
                # Previous partner becomes free again
                men_free.append(current_partner)
            else:
                # Woman prefers current partner
                men_free.append(man)
    
    # Check if matching is complete
    if None in men_partners or None in women_partners or men_free:
        raise ValueError("No stable matching possible")
    
    # Create result dictionary
    result = {}
    for i, partner in enumerate(men_partners):
        result[f'man_{i}'] = f'woman_{partner}'
    
    return result