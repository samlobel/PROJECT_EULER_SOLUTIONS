

"""

So, it's pretty clear we just need n-1 edges for n vertices.
Which means that we just need to add edges in order of completeness, each
time testing to see if there are any cycles.
Because, to link any thing to the graph, if you go in order of small edges,
there will never be a time where a longer route is better.


So, what I should do have two sets, things I've seen and things I'm yet to
see. And look at all edges that lead from something we have to something we don't.
Then, add the smallest one. Then recompute the edges that matter to me.


So, have two sets, seen and not seen. Also have a set of all edges.
Filter the edges so that v1 is in seen and v2 is in not seen. Rank by size.
choose, and add it. Then, move that edge from not seen to seen. Repeat.
Easy as pie. The hardest part is going to be making this matrix into what I
need.

"""





