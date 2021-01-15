-- public.metrics definition

-- Drop table

DROP TABLE public.metrics;

CREATE TABLE public.metrics (
	registered_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	jobname varchar(10) NOT NULL,
	jobtype varchar(3) NOT NULL,
    metric varchar(15) NOT NULL,
	value float8 NOT NULL,
	CONSTRAINT metrics2_pk PRIMARY KEY (registered_at, jobname, jobtype, metric)
);
CREATE INDEX metrics2_jobtype_idx ON public.metrics USING btree (jobtype, jobname);
GRANT ALL ON public.metrics to grafana;