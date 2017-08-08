def merge_list_items_on_predicate(items, callable_predicate, callable_merger):
    """ Merges list items that validate a given predicate, through a given merger.

    It generates a new list.

    >>> items = [(4, 5), (5, 8), (15, 16), (23, 24), (24, 27), (27, 35), (35, 42),]
    >>> merged_items = merge_list_items_on_predicate(
    ...     items=items,
    ...     callable_predicate=lambda first, second: first[1] == second[0],
    ...     callable_merger=lambda first, second: (first[0], second[1]),
    ... )
    >>> merged_items
    [(4, 8), (15, 16), (23, 42)]

    >>> items = [1]
    >>> merged_items = merge_list_items_on_predicate(
    ...     items=items,
    ...     callable_predicate=lambda first, second: first == second,
    ...     callable_merger=lambda first, second: first,
    ... )
    >>> merged_items
    [1]

    :param list items: The input list
    :param callable_predicate: A callable that takes two elements as arguments
        and should return a boolean to say if the two given (consecutive) items
        should be merged or not.
    :param callable_merger: A callable that takes two elements as arguments and
        returns a new "merged" element.
    :return: The list with merged elements.
    """
    new_list = []
    if len(items) >= 2:
        new_list.append(items[0])
        for item in items[1:]:
            if callable_predicate(new_list[-1], item):
                new_list[-1] = callable_merger(new_list[-1], item)
            else:
                new_list.append(item)
    else:
        new_list = items
    return new_list


if __name__ == '__main__':
    import doctest
    doctest.testmod()
