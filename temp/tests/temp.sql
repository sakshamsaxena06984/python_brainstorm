insert into table_name (ppln_id, ppln_vsn_no, dag_id, dag_run_id)
select (single_run_record ->> 'ppln_id') AS ppln_id,
       (single_run_record ->> 'ppln_vsn_no') AS ppln_vsn_no,
       (single_run_record ->> 'dag_id') AS dag_id,
       (single_run_record ->> 'dag_run_id') AS dag_run_id
      from jsonb_array_elements(event_dtl_jsonb_tx -> 'runs') AS single_run_record
      on conflict(dag_id, dag_run_id)
        do update
         set ppln_id = EXCLUDED.ppln_id
             ppln_vsn_no = EXCLUDED.ppln_vsn_no

// 29902910185721
[
 {
   'ppln_id':123,
   'ppln_vsn_no':2,
   'dag_id':'dag_123_pipe',
    'dag_run_id':'dag_123_pipe_v1'
 },
 {
   'ppln_id':124,
   'ppln_vsn_no':21,
   'dag_id':'dag_1234_pipe',
   'dag_run_id':'dag_1234_pipe_v1'
 },
]


