import pytest
from src.stable_marriage import stable_marriage

def test_basic_stable_marriage():
    """Test a simple stable marriage scenario."""
    preferences = {
        'men': [
            [0, 1],  # man 0's preferences
            [1, 0]   # man 1's preferences
        ],
        'women': [
            [1, 0],  # woman 0's preferences
            [0, 1]   # woman 1's preferences
        ]
    }
    result = stable_marriage(preferences)
    assert result == {'man_0': 'woman_0', 'man_1': 'woman_1'}

def test_complex_stable_marriage():
    """Test a more complex stable marriage scenario."""
    preferences = {
        'men': [
            [0, 1, 2],
            [1, 2, 0],
            [2, 0, 1]
        ],
        'women': [
            [1, 2, 0],
            [2, 0, 1],
            [0, 1, 2]
        ]
    }
    result = stable_marriage(preferences)
    
    # Validate result
    assert len(result) == 3
    
    # Check that each person is matched
    for i in range(3):
        assert f'man_{i}' in result
        assert result[f'man_{i}'].startswith('woman_')

def test_invalid_input_empty():
    """Test handling of empty preferences."""
    with pytest.raises(ValueError, match="Preferences must contain 'men' and 'women' keys"):
        stable_marriage({})

def test_unbalanced_groups():
    """Test handling of unequal group sizes."""
    unbalanced_preferences = {
        'men': [[0, 1], [1, 0]],
        'women': [[0]]
    }
    with pytest.raises(ValueError, match="Number of men and women must be equal"):
        stable_marriage(unbalanced_preferences)

def test_impossible_matching():
    """Test scenario where no stable matching is possible."""
    impossible_preferences = {
        'men': [
            [1, 0],  # Prefer partner of the other preference item
            [0, 1]
        ],
        'women': [
            [0, 1],  # Same issue from women's side
            [1, 0]
        ]
    }
    with pytest.raises(ValueError, match="No stable matching possible"):
        stable_marriage(impossible_preferences)

def test_result_properties():
    """Verify key properties of the stable marriage result."""
    preferences = {
        'men': [
            [0, 1, 2],
            [1, 2, 0],
            [2, 0, 1]
        ],
        'women': [
            [1, 2, 0],
            [2, 0, 1],
            [0, 1, 2]
        ]
    }
    result = stable_marriage(preferences)
    
    # Verify bijection
    men_matched = {k for k in result.keys()}
    women_matched = {result[k] for k in result.keys()}
    
    assert len(men_matched) == len(women_matched)
    assert len(men_matched) == len(preferences['men'])

def verify_stability(preferences, matches):
    """
    Verify the stability of the matching.
    A matching is stable if no man-woman pair would both prefer each other 
    over their current partners.
    """
    for man_index in range(len(preferences['men'])):
        man_pref = preferences['men'][man_index]
        current_woman = int(matches[f'man_{man_index}'].split('_')[1])
        
        for potential_woman_index in man_pref:
            # Skip current partner
            if potential_woman_index == current_woman:
                break
            
            woman_pref = preferences['women'][potential_woman_index]
            current_woman_partner = int(
                [k for k, v in matches.items() if v == f'woman_{potential_woman_index}'][0].split('_')[1]
            )
            
            # Check if both would prefer each other
            if (woman_pref.index(man_index) < woman_pref.index(current_woman_partner) and
                man_pref.index(potential_woman_index) < man_pref.index(current_woman)):
                assert False, f"Unstable match between man {man_index} and woman {potential_woman_index}"

def test_matching_stability():
    """Comprehensive test for matching stability."""
    preferences = {
        'men': [
            [0, 1, 2],
            [1, 2, 0],
            [2, 0, 1]
        ],
        'women': [
            [1, 2, 0],
            [2, 0, 1],
            [0, 1, 2]
        ]
    }
    result = stable_marriage(preferences)
    verify_stability(preferences, result)