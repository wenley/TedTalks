
import sqlite3
from talk import Talk

connection = sqlite3.connect('talks.sqlite')

def init_db():
  cursor = connection.cursor()
  c.execute('''CREATE TABLE talks (url text, author text, title text)''')
  connection.commit()

def load_talk(cursor, url):
  talk = Talk(url)
  cursor.execute('''INSERT INTO talks VALUES ('%s', '%s', '%s')''' % (talk.url, talk.author(), talk.title()))

def test_talks(data):
  talks = map(lambda url: Talk(url), data)
  def helper(talk):
    print "Loading", talk.url
    try:
      return talk.speaker()
    except:
      print "Failed"
      return None
  speakers = map(helper, talks)
  print speakers
  speakers = map(helper, talks)

def verify_no_transcript():
  problematic_talks = [
    'http://www.ted.com/talks/ken_robinson_changing_education_paradigms',
    'http://www.ted.com/talks/diane_j_savino_the_case_for_same_sex_marriage',
    'http://poptech.org/popcasts/dan_nocera_personalized_energy',
    'http://www.ted.com/talks/srikumar_rao_plug_into_your_hard_wired_happiness',
    'http://www.ted.com/talks/bobby_mcferrin_hacks_your_brain_with_music',
    'http://www.ted.com/talks/jesse_schell_when_games_invade_real_life',
  ]

  def helper(url):
    print url
    try:
      Talk(url).speaker()
    except Exception as e:
      print e
  map(helper, problematic_talks)
  # All came back as 404

if __name__ == '__main__':
  data = [
    'http://www.ted.com/talks/hans_rosling_shows_the_best_stats_you_ve_ever_seen',
    'http://www.ted.com/talks/hans_rosling_religions_and_babies',
    'http://www.ted.com/talks/hans_rosling_the_truth_about_hiv',
    'http://www.ted.com/talks/hans_rosling_at_state',
    'http://www.ted.com/talks/hans_rosling_on_global_population_growth',
    'http://www.ted.com/talks/hans_rosling_and_the_magic_washing_machine',
    'http://www.ted.com/talks/hans_rosling_reveals_new_insights_on_poverty',
    'http://www.ted.com/talks/hans_rosling_the_good_news_of_the_decade',
    'http://www.ted.com/talks/hans_rosling_asia_s_rise_how_and_when',
    'http://www.ted.com/talks/ken_robinson_says_schools_kill_creativity',
    'http://www.ted.com/talks/sir_ken_robinson_bring_on_the_revolution',
    # 'http://www.ted.com/talks/ken_robinson_changing_education_paradigms',
    'http://www.ted.com/talks/ken_robinson_how_to_escape_education_s_death_valley',
    'http://www.ted.com/talks/clay_shirky_how_cellphones_twitter_facebook_can_make_history',
    'http://www.ted.com/talks/clay_shirky_how_cognitive_surplus_will_change_the_world',
    'http://www.ted.com/talks/clay_shirky_how_the_internet_will_one_day_transform_government',
    'http://www.ted.com/talks/clay_shirky_on_institutions_versus_collaboration',
    'http://www.ted.com/talks/defend_our_freedom_to_share_or_why_sopa_is_a_bad_idea',
    'http://www.ted.com/talks/sugata_mitra_build_a_school_in_the_cloud',
    'http://www.ted.com/talks/sugata_mitra_the_child_driven_education',
    'http://www.ted.com/talks/sugata_mitra_shows_how_kids_teach_themselves',
    'http://www.ted.com/talks/derek_sivers_how_to_start_a_movement',
    'http://www.ted.com/talks/derek_sivers_weird_or_just_different',
    'http://www.ted.com/talks/derek_sivers_keep_your_goals_to_yourself',
    'http://www.ted.com/talks/julian_treasure_why_architects_need_to_use_their_ears',
    'http://www.ted.com/talks/julian_treasure_the_4_ways_sound_affects_us',
    'http://www.ted.com/talks/julian_treasure_how_to_speak_so_that_people_want_to_listen',
    'http://www.ted.com/talks/julian_treasure_5_ways_to_listen_better',
    'http://www.ted.com/talks/julian_treasure_shh_sound_health_in_8_steps',
    'http://www.ted.com/talks/dan_barber_how_i_fell_in_love_with_a_fish',
    'http://www.ted.com/talks/dan_barber_s_surprising_foie_gras_parable',
    'http://www.ted.com/talks/jamie_oliver',
    'http://www.ted.com/talks/jonas_eliasson_how_to_solve_traffic_jams',
    'http://www.ted.com/talks/amanda_burden_how_public_spaces_make_cities_work',
    'http://www.ted.com/talks/gary_slutkin_let_s_treat_violence_like_a_contagious_disease',
    'http://www.ted.com/talks/catherine_mohr_builds_green',
    'http://www.ted.com/talks/john_kasaona_from_poachers_to_caretakers',
    'http://www.ted.com/talks/rob_dunbar',
    'http://www.ted.com/talks/johan_rockstrom_let_the_environment_guide_our_development',
    'http://www.ted.com/talks/leyla_acaroglu_paper_beats_plastic_how_to_rethink_environmental_folklore',
    'http://www.ted.com/talks/chris_mcknett_the_investment_logic_for_sustainability',
    'http://www.ted.com/talks/peter_attia_what_if_we_re_wrong_about_diabetes',
    'http://www.ted.com/talks/jeremy_jackson',
    'http://www.ted.com/talks/alan_siegel_let_s_simplify_legal_jargon',
    'http://www.ted.com/talks/philip_howard',
    'http://www.ted.com/talks/michael_sandel_the_lost_art_of_democratic_debate',
    'http://www.ted.com/talks/lawrence_lessig_we_the_people_and_the_republic_we_must_reclaim',
    # 'http://www.ted.com/talks/diane_j_savino_the_case_for_same_sex_marriage',
    'http://www.ted.com/talks/tim_jackson_s_economic_reality_check',
    'http://www.ted.com/talks/dambisa_moyo_is_china_the_new_idol_for_emerging_economies',
    'http://www.ted.com/talks/david_puttnam_what_happens_when_the_media_s_priority_is_profit',
    'http://www.ted.com/talks/toby_eccles_invest_in_social_change',
    'http://www.ted.com/talks/elizabeth_pisani_sex_drugs_and_hiv_let_s_get_rational_1',
    'http://www.ted.com/talks/nalini_nadkarni_life_science_in_prison',
    'http://www.ted.com/talks/mechai_viravaidya_how_mr_condom_made_thailand_a_better_place',
    'http://www.ted.com/talks/ethan_zuckerman',
    'http://www.ted.com/talks/chris_anderson_how_web_video_powers_global_innovation',
    'http://www.ted.com/talks/jason_clay_how_big_brands_can_save_biodiversity',
    'http://www.ted.com/talks/sheryl_wudunn_our_century_s_greatest_injustice',
    'http://www.ted.com/talks/dan_pallotta_the_way_we_think_about_charity_is_dead_wrong',
    'http://www.ted.com/talks/michael_sandel_why_we_shouldn_t_trust_markets_with_our_civic_life',
    'http://www.ted.com/talks/aditi_shankardass_a_second_opinion_on_learning_disorders',
    'http://www.ted.com/talks/david_anderson_your_brain_is_more_than_a_bag_of_chemicals',
    'http://www.ted.com/talks/stefan_larsson_what_doctors_can_learn_from_each_other',
    'http://www.ted.com/talks/paul_piff_does_money_make_you_mean',
    'http://www.ted.com/talks/dan_meyer_math_curriculum_makeover',
    'http://www.ted.com/talks/david_cameron',
    'http://www.ted.com/talks/sendhil_mullainathan',
    'http://www.ted.com/talks/michael_specter_the_danger_of_science_denial',
    'http://www.ted.com/talks/sam_harris_science_can_show_what_s_right',
    'http://www.ted.com/talks/nicholas_christakis_the_hidden_influence_of_social_networks',
    'http://www.ted.com/talks/stephen_wolfram_computing_a_theory_of_everything',
    'http://www.ted.com/talks/tim_berners_lee_the_year_open_data_went_worldwide',
    'http://www.ted.com/talks/cameron_herold_let_s_raise_kids_to_be_entrepreneurs',
    'http://www.ted.com/talks/matt_ridley_when_ideas_have_sex',
    'http://www.ted.com/talks/bjarke_ingels_3_warp_speed_architecture_tales',
    'http://www.ted.com/talks/nic_marks_the_happy_planet_index',
    'http://www.ted.com/talks/carne_ross_an_independent_diplomat',
    'http://www.ted.com/talks/boyd_varty_what_i_learned_from_nelson_mandela',
    'http://www.ted.com/talks/michael_pritchard_invents_a_water_filter',
    'http://www.ted.com/talks/adam_grosser_and_his_sustainable_fridge',
    'http://www.ted.com/talks/nathan_myhrvold_could_this_laser_zap_malaria',
    'http://www.ted.com/talks/krista_donaldson_the_80_prosthetic_knee_that_s_changing_lives',
    # 'http://poptech.org/popcasts/dan_nocera_personalized_energy',
    'http://www.ted.com/talks/paul_stamets_on_6_ways_mushrooms_can_save_the_world',
    'http://www.ted.com/talks/geraldine_hamilton_body_parts_on_a_chip',
    'http://www.ted.com/talks/andreas_raptopoulos_no_roads_there_s_a_drone_for_that',
    'http://www.ted.com/talks/guy_hoffman_robots_with_soul',
    'http://www.ted.com/talks/mark_kendall_demo_a_needle_free_vaccine_patch_that_s_safer_and_way_cheaper',
    'http://www.ted.com/talks/eric_topol_the_wireless_future_of_medicine',
    'http://www.ted.com/talks/jeff_han_demos_his_breakthrough_touchscreen',
    'http://www.ted.com/talks/john_la_grou_plugs_smart_power_outlets_1',
    'http://www.ted.com/talks/eric_giler_demos_wireless_electricity',
    'http://www.ted.com/talks/anthony_atala_growing_organs_engineering_tissue',
    'http://www.ted.com/talks/david_merrill_demos_siftables_the_smart_blocks',
    'http://www.ted.com/talks/daniel_kraft_invents_a_better_way_to_harvest_bone_marrow',
    'http://www.ted.com/talks/tan_le_a_headset_that_reads_your_brainwaves',
    'http://www.ted.com/talks/fabian_hemmert_the_shape_shifting_future_of_the_mobile_phone',
    'http://www.ted.com/talks/bonnie_bassler_on_how_bacteria_communicate',
    'http://www.ted.com/talks/jack_andraka_a_promising_test_for_pancreatic_cancer_from_a_teenager',
    'http://www.ted.com/talks/max_little_a_test_for_parkinson_s_with_a_phone_call',
    'http://www.ted.com/talks/ramesh_raskar_a_camera_that_takes_one_trillion_frames_per_second',
    'http://www.ted.com/talks/wolfgang_kessling_how_to_air_condition_outdoor_spaces',
    'http://www.ted.com/talks/rupal_patel_synthetic_voices_as_unique_as_fingerprints',
    'http://www.ted.com/talks/mary_lou_jepsen_could_future_devices_read_images_from_our_brains',
    'http://www.ted.com/talks/ajit_narayanan_a_word_game_to_communicate_in_any_language',
    'http://www.ted.com/talks/hugh_herr_the_new_bionics_that_let_us_run_climb_and_dance',
    'http://www.ted.com/talks/gary_flake_is_pivot_a_turning_point_for_web_exploration',
    'http://www.ted.com/talks/simon_sinek_how_great_leaders_inspire_action',
    'http://www.ted.com/talks/dan_buettner_how_to_live_to_be_100',
    'http://www.ted.com/talks/elizabeth_gilbert_on_genius',
    'http://www.ted.com/talks/richard_st_john_success_is_a_continuous_journey',
    'http://www.ted.com/talks/dan_gilbert_asks_why_are_we_happy',
    'http://www.ted.com/talks/barry_schwartz_on_the_paradox_of_choice',
    'http://www.ted.com/talks/dan_ariely_asks_are_we_in_control_of_our_own_decisions',
    'http://www.ted.com/talks/david_byrne_how_architecture_helped_music_evolve',
    # 'http://www.ted.com/talks/srikumar_rao_plug_into_your_hard_wired_happiness',
    'http://www.ted.com/talks/philip_zimbardo_prescribes_a_healthy_take_on_time',
    'http://www.ted.com/talks/chip_conley_measuring_what_makes_life_worthwhile',
    'http://www.ted.com/talks/elif_shafak_the_politics_of_fiction',
    'http://www.ted.com/talks/sheena_iyengar_on_the_art_of_choosing',
    'http://www.ted.com/talks/steven_johnson_where_good_ideas_come_from',
    'http://www.ted.com/talks/daniel_h_cohen_for_argument_s_sake',
    'http://www.ted.com/talks/jinsop_lee_design_for_all_5_senses',
    'http://www.ted.com/talks/joshua_prager_in_search_for_the_man_who_broke_my_neck',
    'http://www.ted.com/talks/andrew_solomon_love_no_matter_what',
    'http://www.ted.com/talks/danny_hillis_back_to_the_future_of_1994',
    'http://www.ted.com/talks/amy_cuddy_your_body_language_shapes_who_you_are',
    'http://www.ted.com/talks/david_steindl_rast_want_to_be_happy_be_grateful',
    'http://www.ted.com/talks/sally_kohn_let_s_try_emotional_correctness',
    'http://www.ted.com/talks/stephen_cave_the_4_stories_we_tell_ourselves_about_death',
    'http://www.ted.com/talks/philip_evans_how_data_will_transform_business',
    'http://www.ted.com/talks/rory_bremner_s_one_man_world_summit',
    'http://www.ted.com/talks/scott_kim_takes_apart_the_art_of_puzzles',
    'http://www.ted.com/talks/gary_lauder_s_new_traffic_sign_take_turns',
    # 'http://www.ted.com/talks/bobby_mcferrin_hacks_your_brain_with_music',
    'http://www.ted.com/talks/beau_lotto_optical_illusions_show_how_we_see',
    'http://www.ted.com/talks/theo_jansen_creates_new_creatures',
    'http://www.ted.com/talks/adora_svitak',
    # 'http://www.ted.com/talks/jesse_schell_when_games_invade_real_life',
    'http://www.ted.com/talks/tom_wujec_build_a_tower',
    'http://www.ted.com/talks/robert_full_learning_from_the_gecko_s_tail',
    'http://www.ted.com/talks/laurie_santos',
    'http://www.ted.com/talks/paul_ewald_asks_can_we_domesticate_germs',
    'http://www.ted.com/talks/bob_mankoff_anatomy_of_a_new_yorker_cartoon',
    'http://www.ted.com/talks/eleanor_longden_the_voices_in_my_head',
    'http://www.ted.com/talks/derek_paravicini_and_adam_ockelford_in_the_key_of_genius',
    'http://www.ted.com/talks/shane_koyczan_to_this_day_for_the_bullied_and_beautiful',
    'http://www.ted.com/talks/amy_webb_how_i_hacked_online_dating',
    'http://www.ted.com/talks/suzana_herculano_houzel_what_is_so_special_about_the_human_brain',
    'http://www.ted.com/talks/nicolas_perony_puppies_now_that_i_ve_got_your_attention_complexity_theory',
  ]

  # Verify talks have transcripts
  test_talks(data[:2])
  # Some don't - comment out those that don't

  # verify_no_transcript()
