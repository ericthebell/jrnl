# Copyright © 2012-2023 jrnl contributors
# License: https://www.gnu.org/licenses/gpl-3.0.html

# format example, delete later
# OneLineMessage = T(
#     en="something",
#     ja="何か",
# )
# MultiLineMessage = T(
#     en="""
#     something
#     """,
#     ja="""
#     何か
#     """,
# )

from enum import Enum


class MsgText(Enum):
    def __str__(self) -> str:
        return self.value

    # -- Welcome --- #
    WelcomeToJrnl = T(
        en="""
        Welcome to jrnl {version}!

        It looks like you've been using an older version of jrnl until now. That's
        okay - jrnl will now upgrade your configuration and journal files. Afterwards
        you can enjoy all of the great new features that come with jrnl 2:

        - Support for storing your journal in multiple files
        - Faster reading and writing for large journals
        - New encryption back-end that makes installing jrnl much easier
        - Tons of bug fixes

        Please note that jrnl 1.x is NOT forward compatible with this version of jrnl.
        If you choose to proceed, you will not be able to use your journals with
        older versions of jrnl anymore.
        """,
        ja="""
        jrnl {version} へようこそ!

        これまでは古いバージョンの jrnl を使用していたようです。問題ありません。jrnl はこれから
        設定ファイルとジャーナル ファイルをアップグレードします。その後は、jrnl 2 に付属する
        すばらしい新機能をすべてお楽しめます:

        - ジャーナルを複数のファイルに保存するためのサポート
        - 大きなジャーナルの読み取りと書き込みの高速化
        - jrnl のインストールを大幅に容易にする新しい暗号化バックエンド
        - 多数のバグ修正

        jrnl 1.x は、このバージョンの jrnl と前方互換性がありませんのでご注意ください。
        続行する場合は、古いバージョンの jrnl ではジャーナルを使用できなくなります。
        """,
        )

    AllDoneUpgrade = T(
        en="We're all done here and you can start enjoying jrnl 2",
        ja="これですべて完了です、jrnl 2 をお楽しみください",
        )
    
    InstallComplete = T(
        en="""
        jrnl configuration created at {config_path}
        For advanced features, read the docs at https://jrnl.sh
        """,
        ja="""
        jrnl 構成がここに作成されました： {config_path} 
        高度な機能については、https://jrnl.sh のドキュメントをお読みください。
        """,
        )

    # --- Prompts --- #
    InstallJournalPathQuestion = T(
        en="""
        Path to your journal file (leave blank for {default_journal_path}):
        """,
        ja="""
        ジャーナル ファイルへのパス ({default_journal_path} で良ければ空白のままにしてください):
        """,
        )
    DeleteEntryQuestion = T(
        en="Delete entry '{entry_title}'?",
        ja="エントリ '{entry_title}' を削除しますか?",
        )
    ChangeTimeEntryQuestion = T(
        en="Change time for '{entry_title}'?",
        ja="'{entry_title}' の時間を変更しますか？",
        )
    EncryptJournalQuestion = T(
        en="""
        Do you want to encrypt your journal? (You can always change this later)
        """,
        ja="""
        ジャーナルを暗号化しますか？（これは後でいつでも変更できます）
        """,
        )
    UseColorsQuestion = T(
        en="""
        Do you want jrnl to use colors to display entries? (You can always change this later)
        """,  # noqa: E501 - the line is still under 88 when dedented
        ja="""
        jrnl でエントリの表示に色を使用しますか？（これは後でいつでも変更できます）
        """,
        )
    YesOrNoPromptDefaultYes = "[Y/n]"
    YesOrNoPromptDefaultNo = "[y/N]"
    ContinueUpgrade = T(
        en="Continue upgrading jrnl?",
        ja="jrnl のアップグレードを続行しますか？",
        )

    # these should be lowercase, if possible in language
    # "lowercase" means whatever `.lower()` returns
    OneCharacterYes = "y"
    OneCharacterNo = "n"

    # --- Exceptions ---#
    Error = T(
        en="Error",
        ja="エラー",
        )
    UncaughtException = T(
        en="""
        {name}
        {exception}

        This is probably a bug. Please file an issue at:
        https://github.com/jrnl-org/jrnl/issues/new/choose
        """,
        ja="""
        {name}
        {exception}

        これはおそらくバグです。問題を報告してください:
        https://github.com/jrnl-org/jrnl/issues/new/choose
        """,
        )

    ConfigDirectoryIsFile = T(
        en="""
        Problem with config file!
        The path to your jrnl configuration directory is a file, not a directory:

        {config_directory_path}

        Removing this file will allow jrnl to save its configuration.
        """,
        ja="""
        構成ファイルに問題があります!
        jrnl 構成ディレクトリへのパスはディレクトリではなくファイルです:

        {config_directory_path}

        このファイルを削除すると、jrnl が構成を保存できるようになります。
        
        """,
        )

    CantParseConfigFile = T(
        en="""
        Unable to parse config file at:
        {config_path}
        """,
        ja="""
        ここにある構成ファイルを解析できません:
        {config_path}
        """,
        )

    LineWrapTooSmallForDateFormat = T(
        en="""
        The provided linewrap value of {config_linewrap} is too small by
        {columns} columns to display the timestamps in the configured time
        format for journal {journal}.

        You can avoid this error by specifying a linewrap value that is larger
        by at least {columns} in the configuration file or by using
        --config-override at the command line
        """,
        ja="""
        
        """,
        )

    CannotEncryptJournalType = T(
        en="""
        The journal {journal_name} can't be encrypted because it is a
        {journal_type} journal.

        To encrypt it, create a new journal referencing a file, export
        this journal to the new journal, then encrypt the new journal.
        """,
        ja="""
        """,
        )

    ConfigEncryptedForUnencryptableJournalType = T(
        en="""
        The config for journal "{journal_name}" has 'encrypt' set to true, but this type
        of journal can't be encrypted. Please fix your config file.
        """,
        ja="""
        """,
        )

    DecryptionFailedGeneric = T(
        en="The decryption of journal data failed.",
        ja="",
        )

    KeyboardInterruptMsg = T(
        en="Aborted by user",
        ja="",
        )

    CantReadTemplate = T(
        en="""
        Unable to find a template file {template_path}.

        The following paths were checked:
         * {jrnl_template_dir}{template_path}
         * {actual_template_path}
        """,
        ja="""
        """,
        )

    NoNamedJournal = T(
        en="No '{journal_name}' journal configured\n{journals}",
        ja="",
        )

    DoesNotExist = T(
        en="{name} does not exist",
        ja="",
        )

    # --- Journal status ---#
    JournalNotSaved = T(
        en="Entry NOT saved to journal",
        ja="",
        )
    JournalEntryAdded = T(
        en="Entry added to {journal_name} journal",
        ja="",
        )

    JournalCountAddedSingular = T(
        en="{num} entry added",
        ja="",
        )
    JournalCountModifiedSingular = T(
        en="{num} entry modified",
        ja="",
        )
    JournalCountDeletedSingular = T(
        en="{num} entry deleted",
        ja="",
        )

    JournalCountAddedPlural = T(
        en="{num} entries added",
        ja="",
        )
    JournalCountModifiedPlural = T(
        en="{num} entries modified",
        ja="",
        )
    JournalCountDeletedPlural = T(
        en="{num} entries deleted",
        ja="",
        )

    JournalCreated = T(
        en="Journal '{journal_name}' created at {filename}",
        ja="",
        )
    DirectoryCreated = T(
        en="Directory {directory_name} created",
        ja="",
        )
    JournalEncrypted = T(
        en="Journal will be encrypted",
        ja="",
        )
    JournalEncryptedTo = T(
        en="Journal encrypted to {path}",
        ja="",
        )
    JournalDecryptedTo = T(
        en="Journal decrypted to {path}",
        ja="",
        )
    BackupCreated = T(
        en="Created a backup at {filename}",
        ja="",
        )

    # --- Editor ---#
    WritingEntryStart = T(
        en="""
        Writing Entry
        To finish writing, press {how_to_quit} on a blank line.
        """,
        ja="""
        """,
        )
    HowToQuitWindows = T(
        en="Ctrl+z and then Enter",
        ja="",
        )
    HowToQuitLinux = T(
        en="Ctrl+d",
        ja="",
        )

    EditorMisconfigured = T(
        en="""
        No such file or directory: '{editor_key}'

        Please check the 'editor' key in your config file for errors:
            editor: '{editor_key}'
        """,
        ja="""
        """,
        )

    EditorNotConfigured = T(
        en="""
        There is no editor configured

        To use the --edit option, please specify an editor your config file:
            {config_file}

        For examples of how to configure an external editor, see:
            https://jrnl.sh/en/stable/external-editors/
        """,
        ja="""
        """,
        )

    NoEditsReceivedJournalNotDeleted = T(
        en="""
        No text received from editor. Were you trying to delete all the entries?

        This seems a bit drastic, so the operation was cancelled.

        To delete all entries, use the --delete option.
        """,
        ja="""
        """,
        )

    NoEditsReceived = T(
        en="No edits to save, because nothing was changed",
        ja="",
        )

    NoTextReceived = T(
        en="""
        No entry to save, because no text was received
        """,
        ja="""
        """,
        )
    NoChangesToTemplate = T(
        en="""
        No entry to save, because the template was not changed
        """,
        ja="""
        """,
        )

    # --- Upgrade --- #
    JournalFailedUpgrade = T(
        en="""
        The following journal{s} failed to upgrade:
        {failed_journals}

        Please tell us about this problem at the following URL:
        https://github.com/jrnl-org/jrnl/issues/new?title=JournalFailedUpgrade
        """,
        ja="""
        """,
        )

    UpgradeAborted = T(
        en="jrnl was NOT upgraded",
        ja="",
        )

    AbortingUpgrade = T(
        en="Aborting upgrade...",
        ja="",
        )

    ImportAborted = T(
        en="Entries were NOT imported",
        ja="",
        )

    JournalsToUpgrade = T(
        en="""
        The following journals will be upgraded to jrnl {version}:

        """,
        ja="""
        """,
        )

    JournalsToIgnore = T(
        en="""
        The following journals will not be touched:

        """,
        ja="""
        """,
        )

    UpgradingJournal = T(
        en="""
        Upgrading '{journal_name}' journal stored in {path}...
        """,
        ja="""
        """,
        )

    UpgradingConfig = T(
        en="Upgrading config...",
        ja="",
        )

    PaddedJournalName = "{journal_name:{pad}} -> {path}"

    # -- Config --- #
    AltConfigNotFound = T(
        en="""
        Alternate configuration file not found at the given path:
            {config_file}
        """,
        ja="""
        """,
        )

    ConfigUpdated = T(
        en="""
        Configuration updated to newest version at {config_path}
        """,
        ja="""
        """,
        )

    ConfigDoubleKeys = T(
        en="""
        There is at least one duplicate key in your configuration file.

        Details:
        {error_message}
        """,
        ja="""
        """,
        )
    # --- Password --- #
    Password = T(
        en="Password:",
        ja="",
        )
    PasswordFirstEntry = T(
        en="Enter password for journal '{journal_name}': ",
        ja="",
        )
    PasswordConfirmEntry = T(
        en="Enter password again: ",
        ja="",
        )
    PasswordMaxTriesExceeded = T(
        en="Too many attempts with wrong password",
        ja="",
        )
    PasswordCanNotBeEmpty = T(
        en="Password can't be empty!",
        ja="",
        )
    PasswordDidNotMatch = T(
        en="Passwords did not match, please try again",
        ja="",
        )
    WrongPasswordTryAgain = T(
        en="Wrong password, try again",
        ja="",
        )
    PasswordStoreInKeychain = T(
        en="Do you want to store the password in your keychain?",
        ja="",
        )

    # --- Search --- #
    NothingToDelete = T(
        en="""
        No entries to delete, because the search returned no results
        """,
        ja="""
        """,
        )
    NothingToModify = T(
        en="""
        No entries to modify, because the search returned no results
        """,
        ja="""
        """,
        )
    NoEntriesFound = T(
        en="no entries found",
        ja="",
        )
    EntryFoundCountSingular = T(
        en="{num} entry found",
        ja="",
        )
    EntryFoundCountPlural = T(
        en="{num} entries found",
        ja="",
        )

    # --- Formats --- #
    HeadingsPastH6 = T(
        en="""
        Headings increased past H6 on export - {date} {title}
        """,
        ja="""
        """,
        )
    YamlMustBeDirectory = T(
        en="""
        YAML export must be to a directory, not a single file
        """,
        ja="""
        """,
        )
    JournalExportedTo = T(
        en="Journal exported to {path}",
        ja="",
        )

    # --- Import --- #
    ImportSummary = T(
        en="""
        {count} imported to {journal_name} journal
        """,
        ja="""
        """,
        )
    # --- Color --- #
    InvalidColor = T(
        en="{key} set to invalid color: {color}",
        ja="",
        )

    # --- Keyring --- #
    KeyringBackendNotFound = T(
        en="""
        Keyring backend not found.

        Please install one of the supported backends by visiting:
          https://pypi.org/project/keyring/
        """,
        ja="""
        """,
        )
    KeyringRetrievalFailure = T(
        en="Failed to retrieve keyring",
        ja="",
        )

    # --- Deprecation --- #
    DeprecatedCommand = T(
        en="""
        The command {old_cmd} is deprecated and will be removed from jrnl soon.
        Please use {new_cmd} instead.
        """,
        ja="""
        """,
        )