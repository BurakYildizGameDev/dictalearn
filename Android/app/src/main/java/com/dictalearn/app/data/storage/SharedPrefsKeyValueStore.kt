package com.dictalearn.app.data.storage

import android.content.Context
import com.dictalearn.app.domain.progress.KeyValueStore

class SharedPrefsKeyValueStore(context: Context, name: String = "dictalearn") : KeyValueStore {
    private val prefs = context.applicationContext.getSharedPreferences(name, Context.MODE_PRIVATE)

    override fun getString(key: String): String? = prefs.getString(key, null)

    override fun putString(key: String, value: String) {
        prefs.edit().putString(key, value).apply()
    }
}
