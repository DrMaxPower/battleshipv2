        # score_player
        counter_row_a_comp = Counter(row_a_comp.values())
        hit_on_row_a_comp = counter_row_a_comp['x']

        counter_row_b_comp = Counter(row_b_comp.values())
        hit_on_row_b_comp = counter_row_b_comp['x']

        counter_row_c_comp = Counter(row_c_comp_hide.values())
        hit_on_row_c_comp = counter_row_c_comp['x']

        counter_row_d_comp = Counter(row_d_comp_hide.values())
        hit_on_row_d_comp = counter_row_d_comp['x']

        score_player += sum(
            [
                hit_on_row_a_comp, hit_on_row_b_comp,
                hit_on_row_c_comp, hit_on_row_d_comp
                ]
            ) 


        # score_computer
        counter_row_a_x = Counter(row_a.values())
        hit_on_row_a_x = counter_row_a_x['x']

        counter_row_b_x = Counter(row_b.values())
        hit_on_row_b_x = counter_row_b_x['x']

        counter_row_c_x = Counter(row_c.values())
        hit_on_row_c_x = counter_row_c_x['x']

        counter_row_d_x = Counter(row_d.values())
        hit_on_row_d_x = counter_row_d_x['x']

        score_computer += sum(

            [hit_on_row_a_x, hit_on_row_b_x, hit_on_row_c_x, hit_on_row_d_x]

            ) - 1