# (C) Datadog, Inc. 2020-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from datadog_checks.dev import get_docker_hostname, get_here
from datadog_checks.dev.jmx import JMX_E2E_METRICS, JVM_E2E_METRICS

CHECK_NAME = "cassandra"

HERE = get_here()
HOST = get_docker_hostname()

"""
# not all metrics will be available in our E2E environment
# it looks like total blocked was not in the `metrics.yaml` file.
# https://blog.pythian.com/guide-to-cassandra-thread-pools
    "cassandra.currently_blocked_tasks",
    "cassandra.total_blocked_tasks",
"""

# For some reason, those two metrics are not provided by cassandra.
CASSANDRA_JVM_METRICS_NOT_PRESENT = {'jvm.gc.cms.count', 'jvm.gc.parnew.time'}

CASSANDRA_JVM_E2E_METRICS = list(set(JVM_E2E_METRICS) - CASSANDRA_JVM_METRICS_NOT_PRESENT)

CASSANDRA_E2E_METRICS = (
    [
        "cassandra.active_tasks",
        "cassandra.timeouts.count",
        "cassandra.timeouts.one_minute_rate",
        "cassandra.bloom_filter_false_ratio",
        "cassandra.bytes_flushed.count",
        "cassandra.cas_commit_latency.75th_percentile",
        "cassandra.cas_commit_latency.95th_percentile",
        "cassandra.cas_commit_latency.one_minute_rate",
        "cassandra.cas_prepare_latency.75th_percentile",
        "cassandra.cas_prepare_latency.95th_percentile",
        "cassandra.cas_prepare_latency.one_minute_rate",
        "cassandra.cas_propose_latency.75th_percentile",
        "cassandra.cas_propose_latency.95th_percentile",
        "cassandra.cas_propose_latency.one_minute_rate",
        "cassandra.col_update_time_delta_histogram.75th_percentile",
        "cassandra.col_update_time_delta_histogram.95th_percentile",
        "cassandra.col_update_time_delta_histogram.min",
        "cassandra.compaction_bytes_written.count",
        "cassandra.compression_ratio",
        "cassandra.currently_blocked_tasks.count",
        "cassandra.db.droppable_tombstone_ratio",
        "cassandra.dropped.one_minute_rate",
        "cassandra.exceptions.count",
        "cassandra.key_cache_hit_rate",
        "cassandra.latency.75th_percentile",
        "cassandra.latency.95th_percentile",
        "cassandra.latency.one_minute_rate",
        "cassandra.live_disk_space_used.count",
        "cassandra.live_ss_table_count",
        "cassandra.load.count",
        "cassandra.max_partition_size",
        "cassandra.max_row_size",
        "cassandra.mean_partition_size",
        "cassandra.mean_row_size",
        "cassandra.net.down_endpoint_count",
        "cassandra.net.up_endpoint_count",
        "cassandra.pending_compactions",
        "cassandra.pending_flushes.count",
        "cassandra.pending_tasks",
        "cassandra.range_latency.75th_percentile",
        "cassandra.range_latency.95th_percentile",
        "cassandra.range_latency.one_minute_rate",
        "cassandra.read_latency.75th_percentile",
        "cassandra.read_latency.95th_percentile",
        "cassandra.read_latency.99th_percentile",
        "cassandra.read_latency.one_minute_rate",
        "cassandra.row_cache_hit.count",
        "cassandra.row_cache_hit_out_of_range.count",
        "cassandra.row_cache_miss.count",
        "cassandra.snapshots_size",
        "cassandra.ss_tables_per_read_histogram.75th_percentile",
        "cassandra.ss_tables_per_read_histogram.95th_percentile",
        "cassandra.tombstone_scanned_histogram.75th_percentile",
        "cassandra.tombstone_scanned_histogram.95th_percentile",
        "cassandra.total_blocked_tasks.count",
        "cassandra.total_commit_log_size",
        "cassandra.total_disk_space_used.count",
        "cassandra.view_lock_acquire_time.75th_percentile",
        "cassandra.view_lock_acquire_time.95th_percentile",
        "cassandra.view_lock_acquire_time.one_minute_rate",
        "cassandra.view_read_time.75th_percentile",
        "cassandra.view_read_time.95th_percentile",
        "cassandra.view_read_time.one_minute_rate",
        "cassandra.waiting_on_free_memtable_space.75th_percentile",
        "cassandra.waiting_on_free_memtable_space.95th_percentile",
        "cassandra.write_latency.75th_percentile",
        "cassandra.write_latency.95th_percentile",
        "cassandra.write_latency.99th_percentile",
        "cassandra.write_latency.one_minute_rate",
    ]
    + CASSANDRA_JVM_E2E_METRICS
    + JMX_E2E_METRICS
)
