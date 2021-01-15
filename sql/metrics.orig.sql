-- public.metrics definition

-- Drop table

-- DROP TABLE public.metrics;

CREATE TABLE public.metrics (
	jobtype varchar(3) NOT NULL,
	jobname varchar(10) NOT NULL,
	ecpu_percent float8 NOT NULL,
	ecpu_time float8 NOT NULL,
	ziip_percent float8 NOT NULL,
	ziip_time float8 NOT NULL,
	registred_at timestamp(0) NOT NULL,
	CONSTRAINT metrics_pk PRIMARY KEY (jobtype, jobname, registred_at)
);
CREATE INDEX metrics_jobtype_idx ON public.metrics USING btree (jobtype, jobname);