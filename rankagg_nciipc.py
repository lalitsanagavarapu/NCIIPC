# Program takes 
import rankaggregation as ra
agg = ra.RankAggregator()
# Bank names in the list
rank_list = [['M','N','O','P'], ['M','O','N','P'], ['M','P','O','N']]
agg.instant_runoff(rank_list)
