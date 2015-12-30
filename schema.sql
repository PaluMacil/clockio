CREATE TABLE alarm (
  id SERIAL PRIMARY KEY,
  name VARCHAR,
  status VARCHAR,
  alarm_time TIME,
  sunday BOOLEAN,
  monday BOOLEAN,
  tuesday BOOLEAN,
  wednesday BOOLEAN,
  thursday BOOLEAN,
  friday BOOLEAN,
  saturday BOOLEAN,
  owner_id INTEGER,
  owner_username VARCHAR,
  created_dtm TIMESTAMP DEFAULT now(),
  modified_dtm TIMESTAMP
);

CREATE FUNCTION alarm_modified() RETURNS TRIGGER
  LANGUAGE plpgsql
  AS $$
BEGIN
  NEW.modified_dtm := current_timestamp;
  RETURN NEW;
END;
$$;

CREATE TRIGGER trigger_alarm_modified
  BEFORE UPDATE ON alarm
  FOR EACH ROW
  EXECUTE PROCEDURE alarm_modified();

select array_to_json((
  select array_agg(row)
  from (select *
        from alarm.alarm) row));

INSERT INTO alarm.alarm (name, status, alarm_time, sunday, monday, tuesday, wednesday, thursday, friday, saturday, owner_id, owner_username)
VALUES ('Work Morning', 'ACTIVE', '06:45', false, true, true, true, true, true, false, 1, 'dan');